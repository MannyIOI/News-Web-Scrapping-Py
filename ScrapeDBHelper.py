import mysql.connector
from mysql.connector import Error


class DB:
    def __init__(self, dbname = "webscrap"):
        try:
            self.conn = mysql.connector.connect(charset='utf8', host="localhost", user="root",
                                               password="", database=dbname, use_unicode=True)

            print("Database is connected successfully")
    
        except Error as e:
            print(e)

    def addNews(self, news):
        query = '''INSERT INTO `news` (`id`, `content`, `created_at`, `description`, `image`, `title`) 
                    VALUES 
                    (NULL, 
                     %s, 
                     %s, 
                     %s, 
                     %s, 
                     %s)
                '''
        args = (news.content, news.created_at, news.description, news.image, news.title.encode('utf8'))
        cursor = self.conn.cursor()
        
        try:
            cursor.execute('SET NAMES utf8;')
            cursor.execute('SET CHARACTER SET utf8;')
            cursor.execute('SET character_set_connection=utf8;')
            cursor.execute(query, args)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()


class News:
    def __init__(self, title, description, content, created_at, image):
        self.title = title
        self.description = description
        self.content = content
        self.created_at = created_at
        self.image = image
