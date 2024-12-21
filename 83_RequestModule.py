import requests
from bs4 import BeautifulSoup
# response = requests.get("https://www.google.com")
# print(response.text)
url = "https://www.google.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h1"):
    print(heading.text)