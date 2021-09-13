import requests
from bs4 import BeautifulSoup
from datetime import datetime

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
        img_url = str(image['src']).replace('..', 'https://books.toscrape.com')
        downloaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = (title, img_url, downloaded_at)
        list_of_rows.append(row)
    return list_of_rows

def scrapeImagesFromAllPages(url):
    list_of_all_rows = []
    main_soup = makeSoup(url)
    pages = findNoOfPages(main_soup)
    print(f'Scraping images from {pages} pages ({20*pages} images):')
    print('============================')
    for page in range(1, pages+1):
        page_url = url + f'/catalogue/page-{page}.html'
        print(f'scrape page {page}:', page_url)
        print('============================')
        rows = scrapeImagesOnPage(page_url)
        list_of_all_rows += rows
    return list_of_all_rows
            




    





