# Project - 6 CS 325 Riwaz Poudel and Justin Burns
## Python Program to scrape comments from multiple reddit post and running sentimental analysis on it
### Description
This project scraps all the user comments from multiple reddit posts stored in a file, and runs a sentimental analysis algorithm on it
### How to make this program run in your device?
#### Installing Anaconda in your device
1. You would need to install Anaconda into your device. Head to anaconda.com and install the latest version of Anaconda to your device.
2. After you have installed the Anaconda, you can check if it was succesfully installed or not by running the following command in your terminal. Mac users can use their terminal whereas Windows user can do this step in the Anaconda python terminal. 
   ```conda activate```
#### Cloning the Project in your device
1. In this github repository, click the green button that says Code.
2. You can see a HTTPS link, copy that to your clipboard.
3. In your terminal, go to your desired folder, where you want to clone this repository
4. Type the following line of code to your terminal
   ```git clone "Paste the HTTPS link you copied earlier, don't include the quotation"```
5. After this command, a local file in your device exists
#### Setting up the conda environment
1. In your terminal change your directory to go inside the CS325_project4 file
2. The project file(CS325_project4) has following modules and files
   ```
   module_1
   module_2
   module_3
   module_4
   Data
   run.py
   reddit.txt(Store the reddit link here. You can store multiple reddit link for this project(New version feature)
   ```
3. The requirement.yaml file has all the necessary packages for this code to work
4. To create a new environment, run the following code in your terminal, env_name can be anything. Make sure its unique and something you have never used before
   ```conda env create --name env_name --file=requirement.yml```
5. This will take few minutes. After succesful activation, run the following code in your terminal. env_name is the name of environment you initialized in previous step
   ```conda activate env_name```
#### Running the program
   
   1. Make sure you have your environment working before you run your python script.
   2. Run the following command
      ```python run.py reddit.txt ```
      Instead of reddit.txt, you can also have any file you want to run the program. Make sure you give the correct directory
   4. The scraped comment will be stored in Data/processed directory as comment_1.txt, comment_2.txt.... based on the links on reddit.txt
   5. The sentiments will be stored in Data/sentiment. In this project, sentiments from only 50 comments from comment1.txt are stored because of the limitation of API
   7. The sentiments will be stored as sentiment1.txt, sentiment2.txt, etc.
   8. The plots for the sentiment will be stored in Data/Plots directory
   9. The plots will be stored as sentiment_plot1.png, sentiment_plot2.png, etc.

#### The process of creating/utilizing keys with openAI/API account.
   1. Before starting, navigate to **'auth0.openai.com'** to create an account.
   2. Once the account is created, navigate through the left-hand-side navigation bar and open **'API keys'**. From here, you can **'Create new secret key'** which gets used in your program.
   3. Inside of your module you wish to utilize openai, you need to first import 'openai'**(It's important to use pip through terminal to install openai first, 'pip install openai')**.
   4. Next, initiliaze your apikey variable in your working '.py' file. **'openai.api_key'** will be set equal to this variable. Also, you'll want to initialize a string variable that will hold the input you wish to hand off to openai for a response. This will be used later.
   5. Now, you must create your '**Chat Completions API**'. This will allow you to make use of one-way conversations with AI to receive responses. Here, you will make use of the input variable you initialized(ai-input). Search for examples of openai's **'openai.Completion.create()'** procedure, and fill out the requested information with your choices of input. This will go below everything you've written so far.
   6. Finally, to extract a response. There are many ways to do so, they all involve utilizing the 'Chat Completions API' entity. Once you've choosen a way to do so, you can save this information within a chosen variable. Here's an example of how we got some feedback/response from our **'Chat Completions API'** entity named **'feedback'**. Example -> **'ai_sentiment = feedback.choices[0].text.strip()'**. Now you've successfully made an API  call.
