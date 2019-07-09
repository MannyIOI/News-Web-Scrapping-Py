##import mysql.connector
##try:
##    con = mysql.connector.connect(host="localhost", user="root",password="", database="webscrap")
##    print("Database is connected successfully")
##    
##except:
##    print("some error")

import requests
from bs4 import BeautifulSoup
from ScrapeImageHelper import read_image
from ScrapeDBHelper import DB
from ScrapeDBHelper import News
import datetime

response = requests.get('https://www.bbc.com/amharic/topics/e986aff5-6b26-4638-b468-371d1d9617b4')
soup = BeautifulSoup(response.text, 'html.parser')

post_container = soup.find(class_="eagle")
posts = post_container.find_all(class_ = "eagle-item")

ERBase = "https://www.bbc.com"
db = DB()
for post in posts:
    ## fetch news title
    titleTag = post.find("a")
    title = titleTag.getText()

    ## fetch news description
    description = post.find(class_="eagle-item__summary").getText()

    #fetch news date
    date = post.find(class_="date").getText()
    
    ## content
    responseI = requests.get(ERBase + titleTag["href"])
    detailSoup = BeautifulSoup(responseI.text, 'html.parser')
    content = detailSoup.find(class_="story-body__inner").getText()
    responseI.close()
    
##
##     

    
    ##image Url
    img = post.find("img")
    imgSrc = None
    if(img != None): imgSrc = img["src"]
##    
##    ## imageBlob
##    imageBlob = None
##    if(imgSrc != None):
##        imageBlob = read_image(imgSrc)

    news = News(title, description, content, datetime.datetime.now(), imgSrc)
    db.addNews(news)
    print("one done")



response.close()




