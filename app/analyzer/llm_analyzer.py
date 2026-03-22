from openai import OpenAI

client = OpenAI()

def analyze_quotes_with_llm(quotes):
    try:
        sample_texts = [q["text"] for q in quotes[:10]]

        prompt = f"""
        Analyze the following quotes and summarize:
        1. Main themes
        2. Emotional tone
        3. Key insights

        Quotes:
        {sample_texts}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("⚠️ LLM调用失败，使用本地分析 fallback")
        return "LLM analysis unavailable (quota exceeded)."