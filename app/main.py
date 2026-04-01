import argparse

from app.task.task_manager import create_task, load_task, run_task as execute_task


def normalize_mode(mode: str) -> str:
    """
    兼容 dashboard 里可能传来的 default。
    """
    if mode in (None, "", "default"):
        return "local"
    return mode


def run_task(pages: int, mode: str):
    mode = normalize_mode(mode)

    task = create_task(mode=mode, pages=pages)
    task_id = task["task_id"]

    print(f"\n🚀 Starting task | task_id={task_id}, pages={pages}, mode={mode}\n")

    execute_task(task_id)

    final_task = load_task(task_id)
    if final_task:
        print(f"✅ Task finished | task_id={task_id}, status={final_task.get('status')}")
    else:
        print(f"⚠️ Task finished but failed to reload task info | task_id={task_id}")

    return task_id


def main():
    parser = argparse.ArgumentParser(description="AI Browser Agent Pipeline")

    parser.add_argument(
        "--pages",
        type=int,
        default=3,
        help="Number of pages to crawl"
    )

    parser.add_argument(
        "--mode",
        type=str,
        default="local",
        choices=["llm", "local", "default"],
        help="Analysis mode: llm / local / default"
    )

    args = parser.parse_args()

    run_task(args.pages, args.mode)


if __name__ == "__main__":
    main()