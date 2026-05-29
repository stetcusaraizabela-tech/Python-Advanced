import requests
from bs4 import BeautifulSoup

url = "https//quotes.toscrape.com"
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    print(len(quotes))
    print(quotes)
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(text)
        print("von:", author)
        print("-" * 30)
else:
    print("Website konnte nicht geladen werden.")
    print("Statuscode:", response.status_code)