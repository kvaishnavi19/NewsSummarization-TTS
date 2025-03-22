import streamlit as st
from utils import fetch_news, analyze_sentiment, extract_topics, generate_comparative_analysis, generate_tts

def main():
    """Streamlit UI for the web app."""
    st.title("📊 News Sentiment Analyzer with Hindi TTS")
    company = st.text_input("Enter company name:")

    if st.button("Fetch News & Analyze"):
        news_articles = fetch_news(company)

        if not news_articles:
            st.error("⚠ No news articles found. Try another company.")
        else:
            # Perform sentiment analysis and extract topics
            for article in news_articles:
                article["Sentiment"] = analyze_sentiment(article["Summary"])
                article["Topics"] = extract_topics(article["Title"], article["Summary"])

            # Generate Comparative Sentiment Analysis
            sentiment_report = generate_comparative_analysis(company, news_articles)

            # Display Results
            st.json(sentiment_report)  # Show structured JSON output
            
            # Generate Hindi Text-to-Speech
            tts_path = generate_tts(sentiment_report["Final Sentiment Analysis"])
            st.audio(tts_path, format="audio/mp3")

if __name__ == "__main__":
    main()
