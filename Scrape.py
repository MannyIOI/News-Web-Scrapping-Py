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

response = requests.get('https://www.ethiopianreporter.com/zena')
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_="item")

ERBase = "https://www.ethiopianreporter.com"
db = DB()
for post in posts:
    ## fetch news title
    titleTag = post.find(class_ = "post-title")
    title = titleTag.getText()

    ## fetch news description
    description = post.find(class_="post-body").getText()

    #fetch news date
    date = post.find(class_="post-created").getText()
    
    ## content
    response = requests.get(ERBase + titleTag.find("a")["href"])
    content = ""
    try:
        detailSoup = BeautifulSoup(response.text, 'html.parser')
        content = detailSoup.find(class_="node__content").getText()
        response.close()
    except:
        print("Something happened ... we skipped this news"
        
    ##image Url
    img = post.find("img")
    imgSrc = None
    if(img != None): imgSrc = ERBase + img["src"]
##    
##    ## imageBlob
##    imageBlob = None
##    if(imgSrc != None):
##        imageBlob = read_image(imgSrc)

    news = News(title, description, content, date, imgSrc)
    db.addNews(news)
    print("one done")



##response.close()




