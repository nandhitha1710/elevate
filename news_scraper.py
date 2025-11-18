import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.ndtv.com/latest"

    # Add user-agent to avoid blocking
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Step 1: Get webpage
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)  # debug
    response.raise_for_status()

    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    # METHOD 1: Try h2 tag
    for tag in soup.find_all("h2", class_="newsHdng"):
        headlines.append(tag.get_text(strip=True))

    # METHOD 2: Try h3 tag (NDTV sometimes uses this)
    for tag in soup.find_all("h3", class_="newsHdng"):
        headlines.append(tag.get_text(strip=True))

    # METHOD 3: Try div container (backup)
    for tag in soup.select("div.news_Itm-cont h2"):
        headlines.append(tag.get_text(strip=True))

    # Save to file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")

    print("Total headlines found:", len(headlines))
    print("Saved to headlines.txt")


scrape_headlines()
