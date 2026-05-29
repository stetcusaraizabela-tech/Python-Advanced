











html = "<span>Hallo</span><span>Welt</span>"
parts = html.split("<span>")
print(parts)
for part in parts:
    if part:
        text = part.split("</span>")[0]
        print(text)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.example.com")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    print(soup.title.text)

