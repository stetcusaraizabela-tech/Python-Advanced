
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    print("Books found:", len(books), "\n")
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text[1]
        stock = book.find("p", class_="stock avalability").text.strip()

        print("Title:", title, "Price:", price, "Stock:", stock)
        print("-" * 30)
else:
    print("Website konnte nicht geladen werden.")
    print("Status code:", response.status_code)