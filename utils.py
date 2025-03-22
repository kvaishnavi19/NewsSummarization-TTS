import requests
from bs4 import BeautifulSoup
import spacy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
from nltk.corpus import stopwords
from googletrans import Translator
from gtts import gTTS

# Download necessary NLTK data
nltk.download("vader_lexicon")
nltk.download("stopwords")

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words("english"))

def fetch_news(company):
    """Fetches latest news articles from Google News RSS."""
    search_url = f"https://news.google.com/rss/search?q={company}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    # Check response status
    if response.status_code != 200:
        print(f"⚠️ Error fetching news. Status: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "lxml-xml")  # Use lxml for XML parsing

    articles = []

    # Extract relevant news items
    for item in soup.find_all("item")[:10]:
        title = item.title.text.strip()
        link = item.link.text.strip()
        summary = item.description.text.strip() if item.description else "No summary available"

        articles.append({"Title": title, "Summary": summary, "Link": link})

    return articles

def analyze_sentiment(text):
    """Performs sentiment analysis on text."""
    score = sia.polarity_scores(text)

    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def extract_topics(title, summary):
    """Extracts key topics using NER & frequency analysis."""
    text = title + " " + summary
    doc = nlp(text)

    named_entities = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "EVENT", "GPE"]]
    words = [word.lower() for word in text.split() if word.lower() not in stop_words and word.isalpha()]
    common_words = [word for word, count in Counter(words).most_common(5)]

    return list(set(named_entities + common_words))

def generate_comparative_analysis(company, articles):
    """Creates a structured sentiment analysis report."""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    comparisons = []
    topic_overlaps = {}

    for article in articles:
        sentiment = analyze_sentiment(article["Summary"])
        article["Sentiment"] = sentiment
        sentiment_counts[sentiment] += 1
        article["Topics"] = extract_topics(article["Title"], article["Summary"])

    for i in range(len(articles) - 1):
        comparison = {
            "Comparison": f"Article {i+1} discusses {articles[i]['Title']}, while Article {i+2} focuses on {articles[i+1]['Title']}.",
            "Impact": f"One highlights {articles[i]['Sentiment']} aspects, while the other covers {articles[i+1]['Sentiment']} sentiments."
        }
        comparisons.append(comparison)

    common_topics = set(articles[0]["Topics"])
    for article in articles:
        common_topics.intersection_update(set(article["Topics"]))

    topic_overlaps = {
        "Common Topics": list(common_topics),
        "Unique Topics": {f"Article {i+1}": article["Topics"] for i, article in enumerate(articles)}
    }

    final_analysis = f"{company} has {sentiment_counts['Positive']} Positive, {sentiment_counts['Negative']} Negative, and {sentiment_counts['Neutral']} Neutral news articles."

    return {
        "Company": company,
        "Articles": articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiment_counts,
            "Coverage Differences": comparisons,
            "Topic Overlap": topic_overlaps
        },
        "Final Sentiment Analysis": final_analysis
    }

def generate_tts(text):
    """Converts sentiment analysis result to Hindi speech."""
    translator = Translator()
    hindi_text = translator.translate(text, src="en", dest="hi").text
    tts = gTTS(text=hindi_text, lang="hi")
    file_path = "output.mp3"
    tts.save(file_path)
    return file_path

# Test with a company name
if __name__ == "__main__":
    company_name = "Google"
    news_articles = fetch_news(company_name)
    
    if news_articles:
        analysis = generate_comparative_analysis(company_name, news_articles)
        print("📊 Final Sentiment Analysis:", analysis["Final Sentiment Analysis"])
        generate_tts(analysis["Final Sentiment Analysis"])
    else:
        print("❌ No news articles found. Please check selectors or change the source.")
