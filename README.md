# Project - 4 CS 325 Riwaz Poudel and Justin Burns
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
2. The project file(reddit_scrapper_v2.0) has following modules and files
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
   3. The scraped comment will be stored in Data/processed directory as comment_1.txt, comment_2.txt.... based on the links on reddit.txt
   4. The sentiments will be stored in Data/sentiment/sentiment1.txt. In this project, sentiments from only 50 comments from comment1.txt are stored because of the limitation of API
   5. Also, due to limitation of the API and frequent change of project documentation, only one reddit link is used in reddit.txt file to keep up the same functionality as project3
