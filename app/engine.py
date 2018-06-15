from bs4 import BeautifulSoup
import requests as r

source = r.get("http://dzienniklodzki.pl").text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('h2'):
    headlines = article.text

print(headlines)

# print(str(soup.prettify))