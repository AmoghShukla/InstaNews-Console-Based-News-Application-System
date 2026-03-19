import os
from config import API_KEY, BASE_URL, Article_file, Summary_file
import requests
import json


def fetch_articles():
    keyword = input("Enter a keyword to search for news articles: ").strip()

    if not keyword:
        print("Please try again! Keyword is Empty.")
        return
    
    parameters = {
        'q' : keyword,
        'apiKey' : API_KEY,
        'language' : 'en'
    }

    response = requests.get(BASE_URL, params=parameters)

    if response.status_code != 200:
        print("Error While Fetching Data : ", response.status_code)
        return
    data = response.json()
    articles = data.get('articles', [])

    valid_articles = []

    for article in articles:
        title = article.get('title')
        author = article.get('author')

        if title and author:
            valid_articles.append(article)
        
        if not title and author:
            print("No Valid Articles Found")
            return
    if not valid_articles:
        print("No Valid Articles Found!!")
        return
    
    with open(Article_file, 'w', encoding='utf-8') as file:
        json.dump(valid_articles, file, indent = 4)
    
    print(f"{len(valid_articles)} valid Articles Saved Successfully!!!")

def Summary():

    if not os.path.exists(Article_file):
        print("No Article Found!!")
        return
    
    with open(Article_file, 'r', encoding="utf-8") as file:
        articles = json.load(file)
    
    with open(Summary_file, "w", encoding="utf-8") as file:
        for article in articles:
            title = article.get("title", "No Title")
            description = article.get("description", "No description")

            file.write(f"Title : {title} \n")
            file.write(f"Description : {description}")
            file.write("="*50 + "\n")

    print("The Article has been summarized and the Summary has been Generated Successfully!!")

def View_Article_Titles():
    if not os.path.exists(Article_file):
        print("No Articel Found !!")
        return
    
    with open(Article_file, 'r', encoding='utf-8') as file:
        articles = json.load(file)
    
    if not articles:
        print("No Valid Articles found")
        return
    print("Article Ttitles : ")
    for i, article in enumerate(articles, start = 1):
            title = article.get('title', 'No Title')
            print(f"{i}. {title}")

def Delete_Article():
    if not os.path.exists(Article_file):
        print("Not Article Found!!")
        return
    os.remove(Article_file)
    print("Article Deleted Successfully!!")

def Exit():
    print("Exiting the Application. Goodbye!")
    return False