from typing import Dict, List, Optional


POSITIVE_TAGS = {
    "inspirational", "hope", "love", "happiness", "success", "courage",
    "friendship", "life", "learning", "wisdom", "peace", "value"
}

NEGATIVE_TAGS = {
    "death", "fear", "heartbreak", "lies", "alcohol", "pain", "regrets",
    "indifference", "hate", "troubles"
}


def infer_theme(tags: List[str], quote: str) -> str:
    if tags:
        return ", ".join(tags[:2])

    q = quote.lower()
    if "love" in q:
        return "love"
    if "life" in q:
        return "life"
    if "book" in q or "read" in q:
        return "reading"
    if "death" in q:
        return "death"
    if "friend" in q:
        return "friendship"
    return "general reflection"


def infer_sentiment(tags: List[str], quote: str) -> str:
    tag_set = {t.lower() for t in tags}

    if tag_set & POSITIVE_TAGS:
        return "positive"
    if tag_set & NEGATIVE_TAGS:
        return "negative"

    q = quote.lower()
    if any(word in q for word in ["love", "hope", "happy", "smile", "courage"]):
        return "positive"
    if any(word in q for word in ["death", "fear", "pain", "hate", "hurt"]):
        return "negative"
    return "neutral"


def infer_tone(tags: List[str], quote: str) -> str:
    tag_set = {t.lower() for t in tags}
    q = quote.lower()

    if "humor" in tag_set or "funny" in q:
        return "humorous"
    if "inspirational" in tag_set:
        return "inspirational"
    if "philosophy" in tag_set or "thinking" in tag_set:
        return "philosophical"
    if "love" in tag_set:
        return "romantic"
    if "death" in tag_set:
        return "serious"
    return "reflective"


def infer_summary(quote: str, author: str, theme: str) -> str:
    short_quote = quote.strip().replace("\n", " ")
    if len(short_quote) > 90:
        short_quote = short_quote[:90] + "..."
    return f'A quote by {author or "Unknown"} about {theme}: {short_quote}'


def analyze_quote_with_llm(
    quote: str,
    author: str = "",
    tags: Optional[List[str]] = None
) -> Dict:
    if tags is None:
        tags = []

    quote = quote.strip()
    author = author.strip()

    if not quote:
        return {
            "ai_theme": "unknown",
            "ai_sentiment": "neutral",
            "ai_tone": "unknown",
            "ai_summary": "No summary available."
        }

    theme = infer_theme(tags, quote)
    sentiment = infer_sentiment(tags, quote)
    tone = infer_tone(tags, quote)
    summary = infer_summary(quote, author, theme)

    return {
        "ai_theme": theme,
        "ai_sentiment": sentiment,
        "ai_tone": tone,
        "ai_summary": summary
    }


def analyze_quotes_with_llm(quotes: List[Dict]) -> str:
    results = []

    for item in quotes:
        quote = item.get("quote", "")
        author = item.get("author", "")
        tags = item.get("tags", [])

        ai_result = analyze_quote_with_llm(
            quote=quote,
            author=author,
            tags=tags
        )

        results.append(
            f'Quote: {quote}\n'
            f'Author: {author}\n'
            f'Theme: {ai_result["ai_theme"]}\n'
            f'Sentiment: {ai_result["ai_sentiment"]}\n'
            f'Tone: {ai_result["ai_tone"]}\n'
            f'Summary: {ai_result["ai_summary"]}\n'
        )

    return ("\n" + "-" * 50 + "\n").join(results)