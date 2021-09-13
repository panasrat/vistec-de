import psycopg2
from config import Config

def image_iterator():
    
    with psycopg2.connect(
        host = Config.HOST,
        database = Config.DATABASE,
        user = Config.USER,
        password = Config.PASSWORD
    ) as connection:
        
        print('Connection established:', connection)
        print('============================')

        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT * FROM scraped_images
                ORDER BY RANDOM()
            ''')
            list_of_images = cursor.fetchall()

    return iter(list_of_images)
