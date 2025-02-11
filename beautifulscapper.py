from bs4 import BeautifulSoup
import requests

# Fetch a webpage
url = "https://service.northeastern.edu/ogs?id=kb_article_view&sys_kb_id=a6cf7f52c38b5614876b72977d01318f"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
title = soup.title.text
links = [a['href'] for a in soup.find_all('a', href=True)]

print("Title:", title)
print("Links:", links)