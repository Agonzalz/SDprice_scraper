import requests
from bs4 import BeautifulSoup

def scrap_ebay(query="steam deck", limit=10):
    search_query = query.replace(" " "+")
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    items = []
    for item in soup.select(".s-item")[:limit]:
        title_elem = item.select_one("s-item__title")
