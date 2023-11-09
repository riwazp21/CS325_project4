import openai


# open_ai key generated from site.
apikey = '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'
openai.api_key = apikey

# Work area for getsentiment function.
def getsentiment(content):

    # String to be sent to ai in order to retrieve sentiment.
    

    ai_input = f"What is the sentiment of the given comment? {content}"

    # Start of request to API
    
    feedback = openai.Completion.create(
        prompt = ai_input,
        engine = "text-davinci-003",
        max_tokens = 60,
        n=1,
        stop=None
    )
    
    # Takes response an parses out sentiment
    ai_sentiment = feedback.choices[0].text.strip()
    return ai_sentiment
#print(getsentiment("I am amazing"))
