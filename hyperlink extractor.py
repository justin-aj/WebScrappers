from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def extract_content_and_hyperlinks(url):
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        # Extract all hyperlinks
        hyperlinks = [a.get_attribute("href")
                      for a in driver.find_elements(By.TAG_NAME, "a")
                      if a.get_attribute("href")]

        # Extract main content (visible text)
        content = driver.find_element(By.TAG_NAME, 'body').text

        return {
            'hyperlinks': hyperlinks,
            'content': content
        }
    finally:
        driver.quit()


# Example usage
url = "https://northeastern.edu/"
result = extract_content_and_hyperlinks(url)

print("Extracted Hyperlinks:")
for link in result['hyperlinks']:
    print(link)

print("\nExtracted Content:")
print(result['content'])