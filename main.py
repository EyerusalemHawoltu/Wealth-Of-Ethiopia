import requests
import time
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://allaboutethio.com/15-richest-ethiopians-and-their-successful-companies.html'

# Define headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

# Function to scrape the website with retry logic
def scrape_website(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            html_content = response.text
            return BeautifulSoup(html_content, 'html.parser')
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            if response.status_code == 429:
                print("Rate limit exceeded, sleeping before retrying...")
                time.sleep(5)  # Wait before retrying
        except Exception as err:
            print(f"An error occurred: {err}")
        time.sleep(2)  # Respectful delay between attempts
    return None

# Function to extract data from the parsed HTML

