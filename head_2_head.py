import requests
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

url = "https://www.ultimatetennisstatistics.com/headToHead"

headers = {"User-Agent": user_agent}


response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
else:
    print("Failed to fetch the page.")
