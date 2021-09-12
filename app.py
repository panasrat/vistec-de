import requests
from bs4 import BeautifulSoup
from datetime import datetime

source = 'https://books.toscrape.com/'

def makeSoup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')

def findNoOfPages(soup):
    tag = soup.find_all('li', {'class': 'current'})
    no_of_pages = int(tag[0].text.strip().split()[-1])
    return no_of_pages

def scrapeImagesOnPage(page_url):
    list_of_rows = []
    soup = makeSoup(page_url)
    images = soup.find_all('img')
    for image in images:
        title = str(image['alt'])
        img_url = str(image['src']).replace('../', source)
        downloaded_at = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        row = (title, img_url, downloaded_at)
        list_of_rows.append(row)
    return list_of_rows

def scrapeImagesFromAllPages(url):
    list_of_all_rows = []
    r = requests.get(url)
    main_soup = BeautifulSoup(r.text, 'html.parser')
    pages = findNoOfPages(main_soup)
    for page in range(1, 4):
        page_url = url + f'/catalogue/page-{page}.html'
        print(page_url)
        print('============================')
        rows = scrapeImagesOnPage(page_url)
        list_of_all_rows += rows
    return list_of_all_rows
            
x = scrapeImagesFromAllPages(source)

print(x[0])





    





