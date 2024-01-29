import requests
from bs4 import BeautifulSoup

# Scraper le site :
# https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html


# Afficher le titre scrapé avec un print()

page = requests.get('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
soup = BeautifulSoup(page.text, 'html.parser')

title = soup.select_one('h1')
description = soup.select_one('div#product_description+p')
price = soup.select_one('p.price_color')



print(title.string)
print(description.string)
print(price.string[2:])

rating = soup.select_one('p.star-rating').get('class')[1]

print(rating)

# rating_mapping = {
#     '1': 'One',
# }
