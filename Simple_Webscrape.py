# pass

import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')

"""
# Create a list of all the quotes on the first page
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
# quotes
"""

# Get all unique authors on the website

url = 'http://quotes.toscrape.com/page/'
page_url = url+str(99999)  # Infinite amount after, meaning page/99999
res = requests.get(page_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
valid_page = True
authors = set()
page = 1
while valid_page:
    page_url = url+str(page)
    res = requests.get(page_url)
    if "No quotes found!" in res.text:  # From the website, I know if the page crosses 10, "No quotes found!" will be displayed
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select(".author"):
        authors.add(name.text)
    page += 1
print(authors)
