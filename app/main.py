from crawler.quotes_spider import crawl_quotes, save_quotes_to_json
from analyzer.quotes_analyzer import analyze_quotes, save_analysis_report
from analyzer.llm_analyzer import analyze_quotes_with_llm


def run():
    # 1. Crawl quote data
    data = crawl_quotes()

    # 2. Save raw crawl data
    save_quotes_to_json(data)

    # 3. Generate statistical analysis report
    report = analyze_quotes(data)
    save_analysis_report(report)

    print("📊 Statistical Analysis Result:")
    print(report)

    # 4. Generate LLM-based analysis
    llm_result = analyze_quotes_with_llm(data)

    # 5. Save LLM analysis result
    with open("data/llm_report.txt", "w", encoding="utf-8") as f:
        f.write(llm_result)

    print("\n🤖 AI Analysis Result:")
    print(llm_result)
    print("✅ LLM analysis saved to data/llm_report.txt")


if __name__ == "__main__":
    run()