import psycopg2
import pandas as pd
from config import Config
from utils import scrapeImagesFromAllPages

def insert_to_postgres(url):

    with psycopg2.connect(
        host = Config.HOST,
        database = Config.DATABASE,
        user = Config.USER,
        password = Config.PASSWORD
    ) as connection:

        print('Connection established:', connection)
        print('============================')
        images = scrapeImagesFromAllPages(url)

        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scraped_images (title VARCHAR, img_url VARCHAR, downloaded_at TIMESTAMP)
            ''')
            cursor.execute('TRUNCATE scraped_images')

            for image in images: 
                cursor.execute('''
                    INSERT INTO scraped_images (title, img_url, downloaded_at) 
                    VALUES (%s, %s, %s)
                ''', image)

            df = pd.read_sql('select * from scraped_images', connection)
            print(df)
        





