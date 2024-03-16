import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

phrases_to_remove = [
    "Your device may not support this visualisation",
    "This video can not be played",
]


def clean_content(text):
    # Join the paragraphs with spaces for readability
    cleaned_text = " ".join(text)

    return cleaned_text


def format_datetime(iso_datetime):
    dt_object = datetime.strptime(iso_datetime, "%Y-%m-%dT%H:%M:%S.%fZ")
    return dt_object.strftime("%B %d, %Y")


def scrape_article(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    parsed_url = urlparse(url)
    source = parsed_url.netloc
    raw_output = []
    soup = BeautifulSoup(response.content, "html.parser")
    text_blocks = soup.select(
        'div[data-component="text-block"]'
    )  # Find "text-block" divs
    for block in text_blocks:
        paragraph = block.find("p")  # Find <p> tag inside the block
        if paragraph:
            raw_output.append(paragraph.text)

    # Assuming some HTML structure:
    title = soup.find("h1", id="main-heading").text.strip()
    source = source
    date_string = soup.find("time").get("datetime")  # Adapt based on the website
    cleaned_text = clean_content(raw_output)

    # Summarize the cleaned content
    summary = summarize_text(cleaned_text)

    # Sentiment Analysis
    vader_score = sid.polarity_scores(cleaned_text)
    print(sid.polarity_scores(cleaned_text))

    # Categorize sentiment
    if vader_score["compound"] > 0:  # Adjust the threshold if needed
        sentiment = "Positive"
    elif vader_score["compound"] < 0:  # Adjust the threshold if needed
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    news_data = {
        "title": title,
        "source": source,
        "publication_date": date_string,
        "summary": summary,
        "sentiment": sentiment,
    }

    return news_data


def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, 5)  # Summarize into 5 sentences
    return " ".join(str(sentence) for sentence in summary_sentences)


# Test it out
if __name__ == "__main__":
    sample_url = (
        "https://www.bbc.co.uk/news/world-europe-68586062"  # Replace with a real URL
    )
    scraped_data = scrape_article(sample_url)
    print(scraped_data)
