import psycopg2
from config import Config

def image_iterator(no_of_images: int):
    
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
                LIMIT %s
            ''', [no_of_images])
            list_of_images = cursor.fetchall()

    return iter(list_of_images)

x = image_iterator(3)
print(next(x))
print(next(x))
print(next(x))