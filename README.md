# NewsSummarization-TTS
News Summarization and  Text-to-Speech Application
News Summarization and Text-to-Speech Application Documentation
1. Project Setup
Installation and Running the Application
Follow these steps to set up and run the application on your local machine:
Prerequisites:
Ensure you have the following installed:
•	Python (version 3.8 or higher)
•	pip (Python package manager)
•	Git
Steps to Install and Run:
1.	Clone the repository
git clone <your-github-repo-link>
cd <repository-folder>
2.	Install dependencies
pip install -r requirements.txt
3.	Run the application
python app.py
4.	Access the application
If deployed on Hugging Face Spaces, visit your space's URL.
If running locally, access via the provided Streamlit UI link.
2. Model Details
Summarization Model
•	Technique Used: Extractive summarization using SpaCy for Named Entity Recognition (NER) and keyword extraction.
•	Purpose: Condenses news articles to highlight key points.
Sentiment Analysis Model
•	Library: NLTK’s Vader (Valence Aware Dictionary and sEntiment Reasoner).
•	Functionality: Classifies sentiment into Positive, Negative, or Neutral.
Text-to-Speech (TTS) Model
•	Library: Google Text-to-Speech (gTTS).
•	Functionality: Converts sentiment analysis results into spoken Hindi text.
•	Translation: Utilizes googletrans to translate text from English to Hindi before speech conversion.

3. API Development
The application provides APIs for:
Endpoints:
1.	Fetch News
o	URL: /fetch_news?company=<company_name>
o	Method: GET
o	Response:
{
  "Title": "News Headline",
  "Summary": "Short description of news article",
  "Link": "URL to the full article"
}
2.	  Sentiment Analysis
o	URL: /analyze_sentiment
o	Method: POST
o	Request Body:
{
  "text": "News summary text"
}
o	Response:
{
  "sentiment": "Positive/Negative/Neutral"
}
3.	Comparative Analysis
o	URL: /comparative_analysis?company=<company_name>
o	Method: GET
o	Response:
{
  "Company": "Google",
  "Sentiment Distribution": {"Positive": 5, "Negative": 3, "Neutral": 2},
  "Topic Overlap": {"Common Topics": ["AI", "Technology"]}
}
4.	Text-to-Speech Conversion
o	URL: /generate_tts
o	Method: POST
o	Request Body:
{
  "text": "Final sentiment analysis result"
}
o	Response: MP3 file for playback.
4. API Usage
Accessing APIs via Postman
•	Import API endpoints into Postman and make GET/POST requests.
•	Ensure JSON responses are formatted correctly.
•	Verify proper API authentication if required.
Third-Party API Integrations
1.	Google News RSS (for fetching news articles).
2.	Google Translate API (for English-to-Hindi translation in TTS).
3.	gTTS API (for generating audio output).
5. Assumptions & Limitations
Assumptions:
•	News articles fetched from Google News RSS contain accurate and structured summaries.
•	Sentiment analysis using Vader is suitable for short text-based summaries.
•	The application will be deployed on Hugging Face Spaces and assumes an internet connection for API calls.
Limitations:
•	Accuracy: Sentiment analysis may not always be accurate for complex sentences.
•	Language Support: TTS conversion is limited to Hindi.
•	API Rate Limits: Google News and Google Translate APIs may impose request limits.
•	Dependency on External Services: If googletrans or gTTS services are down, functionality will be affected.

