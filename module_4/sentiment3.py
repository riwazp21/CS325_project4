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
