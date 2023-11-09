"""
File Name: run.py
Author: Riwaz Poudel
Input: text file that has a reddit url through command line argument
Output: content1.txt, comment1.txt, and sentiment.txt inside Data/Raw, inside Data/Processed, and Data/sentiment respectively
Functionality:
1. This is the main file of the entire program. 
2. This file receives the reddit link through the command line argument
3. The file imports the function content_scraper and comment_scraper from module 1 and module 2
4. The reddit link is passed through the content_scraper
5. The raw file is passed through the comment_scraper
6. The output from this file would be both the raw and processed file of the reddit link that includes html content, and the comments. It will also output the sentiment analysis of the first 50 comments

Basic structure of how the modules work and interact with each other
CS325_p3/
|--run.py
|--module_1
|   └──content_scraper.py
|--module_2
|	└──comment_scraper.py
|--module_3
	└──file_storer.py
|--module_4
        └──sentiment.py
run.py calls functions content_scraper and comment_scraper from module 1 and module 2
content_scraper.py(module_1) and comment_scraper.py(module_2) calls file_storer.py from module_3
After the contents and comments are stored succesfully, run.py calls sentiment.py(module_4) to get the sentiments of a passed comment

"""
from bs4 import BeautifulSoup
from module_1.content_scraper import content_scraper
from module_2.comment_scraper import comment_scraper
from module_4.sentiment3 import get_sentiment

import sys
import os

if __name__ == "__main__":
	url = sys.argv[1]
	count = 1
	content_scraper(url)
	content_path = os.path.join("Data","raw","content1.txt")
	comment_scraper(content_path,count)
	
	sentiment_input_path = os.path.join("Data","processed","comment1.txt")
	sentiment_output_path = os.path.join("Data","sentiment","sentiment1.txt")

	file1 = open(sentiment_input_path,'r')
	file2 = open(sentiment_output_path,'w')
	Lines = file1.readlines()

	count = 0
	for lines in Lines:
		sentiment = get_sentiment(lines)
		#file2.writelines(lines)
		file2.writelines(sentiment)
		file2.writelines("\n")
		count = count + 1
		if(count == 50):
			break
    
	file2.close()
	file1.close()
	print("Sentiment Analysis done succesfully")


# pip install openai -> "Note for prog 4."

