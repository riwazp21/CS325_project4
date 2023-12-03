"""
File Name: run.py
Author: Riwaz Poudel & Justin Burns
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
        └──sentiment3.py
run.py calls functions content_scraper and comment_scraper from module 1 and module 2
content_scraper.py(module_1) and comment_scraper.py(module_2) calls file_storer.py from module_3
After the contents and comments are stored succesfully, run.py calls sentiment3.py(module_4) to get the sentiments of a passed comment

"""
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from module_1.content_scraper import content_scraper
from module_2.comment_scraper import comment_scraper
from module_4.sentiment3 import get_sentiment

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import requests

def sentimentAnalysis(input_file, output_file):
	file1 = open(input_file,'r')
	file2 = open(output_file,'w')
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
    
	file1.close()
	file2.close()
	print("Sentiment Analysis done for " + input_file + " succesfully")



def get_title_from_url(url):
	parsed_url = urlparse(url)
	path_segment = parsed_url.path.split('/')
	desired_part = path_segment[-2]
	formatted_text = ' '.join(word.capitalize() for word in desired_part.split('_'))
	return formatted_text

def title_array_from_file(file):
	titles = []
	with open(file, 'r') as f:
		for line in f:
			title = get_title_from_url(line)
			titles.append(title)
	return titles


if __name__ == "__main__":
	file_name = sys.argv[1]
	count = 1
	content_scraper(file_name)

	#List of all the titles

	url_titles = title_array_from_file(file_name)


	content_path = os.path.join("Data","raw")
	files_list = sorted(os.listdir(content_path))
	for filename in files_list:
		#Made sure the files are sorted alphabetically so that we dont read the wrong file while going through the directory
		file_path = os.path.join(content_path,filename)
		if os.path.isfile(file_path) and filename.endswith('.txt'):
			#print(file_path)
			comment_scraper(file_path, count)
			count = count + 1
	sentiment_input_directory = os.path.join("Data","processed")
	sentiment_output_directory = os.path.join("Data","sentiment")
	count = 1
	##Sentiments are created and written to output files here through sentimentAnalysis which use sentiment function.
	sentiment_file_list = sorted(os.listdir(sentiment_input_directory))
	for filename in sentiment_file_list:
		input_file = os.path.join(sentiment_input_directory,filename)
		#print(input_file)
		if input_file.endswith('.txt'):
			output_file = os.path.join(sentiment_output_directory,"sentiment"+str(count)+".txt")

			sentimentAnalysis(input_file,output_file)
			count = count + 1

	##Implement pandas task here.
count = 1
extracted_path = os.path.join("Data","sentiment")
plot_path = os.path.join("Data","Plots")
plot_file_list = sorted(os.listdir(extracted_path))
colors = {'Positive': 'green', 'Neutral': 'gray', 'Negative': 'red'}
for files in plot_file_list:
    if files.endswith('.txt'):
    	files_to_read = os.path.join(extracted_path,files)
    	with open(files_to_read, 'r') as file:
    		sentiments = file.read().splitlines()
    	positive_count = sentiments.count('Positive')
    	neutral_count = sentiments.count('Neutral')
    	negative_count = sentiments.count('Negative')
    	data = {'Positive':[positive_count],'Neutral':[neutral_count],'Negative':[negative_count]}
    	df = pd.DataFrame(data)
    	ax = df.plot(kind='bar', color=['green', 'grey', 'red'])
    	plt.xlabel('Sentiment')
    	plt.ylabel('Count')
    	plt.title(url_titles[count-1])
    	legend_labels = ['Positive','Neutral','Negative'] 

    	ax.legend(legend_labels)


    	plot_title = 'sentiment_plot' + str(count) + '.png'
    	plot_file_path = os.path.join(plot_path, plot_title)
    	plt.savefig(plot_file_path)
    	print("Sentiment plots stored succesfully \n")
    	count += 1




'''
   #Project 4 stuff
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

  '''
# pip install openai -> "Note for prog 4."

