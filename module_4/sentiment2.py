#Sampel file for testing
#This file conducts the sentiment analysis
from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] = "cwjSgzFrsaHjU9y8RxTngM2HUGDqBq2gsXVHYjyMA88sYTlLZ6_5Y-8h1uashHgMkDK4cQ."



def get_sentiment(text):
	query = "What is the sentiment of the following sentence? Give me one of these three words(Positive, Neutral, Negative)? " + text
	response = Bard().get_answer(str(query))['content']
	return response
	
#print(get_sentiment("I am amazing."))
    
