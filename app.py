from image_iterator import image_iterator
from insert_to_postgres import insert_to_postgres

url = 'https://books.toscrape.com'

insert_to_postgres(url, 300)
x = image_iterator()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
