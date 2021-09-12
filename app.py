import psycopg2
import pandas as pd
from web_scraping import scrapeImagesFromAllPages

url = 'https://books.toscrape.com/'

class Config:
    HOST = 'localhost'
    USER = 'application'
    PASSWORD = 'secretpassword'
    DATABASE = 'application'

with psycopg2.connect(
    host = Config.HOST,
    database = Config.DATABASE,
    user = Config.USER,
    password = Config.PASSWORD
) as connection:

    print(connection)
    images = scrapeImagesFromAllPages(url)

    with connection.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scraped_images (title VARCHAR, img_url VARCHAR, downloaded_at TIMESTAMP)
        ''')

        for image in images: 
            cursor.execute('''
                INSERT INTO scraped_images (title, img_url, downloaded_at) 
                VALUES (%s, %s, %s)
            ''', image)

        df = pd.read_sql('select * from scraped_images limit 10', connection)
        print(df)
        





