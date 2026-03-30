import argparse

from app.crawler.quotes_spider import crawl_quotes, save_quotes_to_json
from app.analyzer.quotes_analyzer import analyze_quotes
from app.analyzer.llm_analyzer import analyze_quotes_with_llm
from app.task.task_manager import create_task, update_task_status


def run_task(pages: int, mode: str):
    task_id, task_dir = create_task(pages, mode)
    print(f"\n🚀 Starting pipeline | task_id={task_id}, pages={pages}, mode={mode}\n")

    try:
        # ===== 1. 抓取数据 =====
        quotes = crawl_quotes(pages)

        # ===== 2. 保存原始数据 =====
        save_quotes_to_json(quotes, f"{task_dir}/quotes_all.json")

        # ===== 3. 本地统计分析 =====
        stats_result = analyze_quotes(quotes)

        print("\n📊 Statistical Analysis Result:")
        print(stats_result)

        # ===== 4. AI分析 =====
        if mode == "llm":
            print("\n🤖 Running LLM analysis...")
            ai_result = analyze_quotes_with_llm(quotes)
        else:
            print("\n🤖 Using local analysis mode...")
            ai_result = "Local mode: LLM skipped. Using statistical insights only."

        print("\n🤖 AI Analysis Result:")
        print(ai_result)

        # ===== 5. 保存AI分析结果 =====
        with open(f"{task_dir}/llm_report.txt", "w", encoding="utf-8") as f:
            f.write(ai_result)

        update_task_status(task_dir, "success")

        print(f"\n✅ Quotes data saved to {task_dir}/quotes_all.json")
        print(f"✅ LLM analysis saved to {task_dir}/llm_report.txt")
        print(f"✅ Task {task_id} finished successfully\n")

        return task_id

    except Exception as e:
        update_task_status(task_dir, "failed", error=e)
        print(f"\n❌ Task {task_id} failed: {e}\n")
        return task_id


def main():
    parser = argparse.ArgumentParser(description="AI Browser Agent Pipeline")

    parser.add_argument(
        "--pages",
        type=int,
        default=10,
        help="Number of pages to crawl"
    )

    parser.add_argument(
        "--mode",
        type=str,
        default="llm",
        choices=["llm", "local"],
        help="Analysis mode: llm or local"
    )

    args = parser.parse_args()

    run_task(args.pages, args.mode)


if __name__ == "__main__":
    main()