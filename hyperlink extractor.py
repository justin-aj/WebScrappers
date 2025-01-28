import requests
from bs4 import BeautifulSoup

def extract_hyperlinks(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all <a> tags with href attributes
        hyperlinks = [a['href'] for a in soup.find_all('a', href=True)]

        return hyperlinks

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

# Example usage
url = "https://www.northeastern.edu/"
hyperlinks = extract_hyperlinks(url)

print("Extracted Hyperlinks:")
for link in hyperlinks:
    print(link)
