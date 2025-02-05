from bs4 import BeautifulSoup
import requests

# Fetch a webpage
url = "https://www.northeastern.edu/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
title = soup.title.text
links = [a['href'] for a in soup.find_all('a', href=True)]

print("Title:", title)
print("Links:", links)