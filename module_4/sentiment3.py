"""
File Name: sentiment3.py
Author: Riwaz Poudel & Justin Burns
Input: Comments or any text that needs a sentiment analysis
Output: sentiment.txt in Data/sentiment
Functionality
1. The function get_sentiment is imported in run.py
2. It calls the textblob API to conduct a sentiment analysis
3. The sentiment of the sentence is returned as either Positive, Negative, or Neutral

"""
from textblob import TextBlob

# Create a list of sentences to analyze


def get_sentiment(sentence):
    analysis = TextBlob(sentence)
    sentiment = analysis.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
