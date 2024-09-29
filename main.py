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
def extract_richest_people(soup):
    if not soup:
        return None
    
    # Extracting all h2 tags
    h2_tags = soup.find_all('h2')
    
    # Filter and clean the names
    names = []
    for h2 in h2_tags:
        text = h2.get_text().strip()
        if text and not text.startswith("The Most Successful and Richest Ethiopians"):
            # Remove any leading index if present
            cleaned_name = text.split('. ', 1)[-1]  # Split and take the part after the first dot
            names.append(cleaned_name)

    return names[:15]  # We are only interested in the first 15 names

# Main function to control the workflow
def main():
    print("Starting web scraping...\n")
    
    # Scrape the website
    soup = scrape_website(url)
    
    if soup:
        # Extract the names of the 15 richest people
        richest_people = extract_richest_people(soup)
        
        # Check if names were found
        if richest_people:
            print("The 15 Richest Ethiopians:\n")
            for i, name in enumerate(richest_people, start=1):
                print(f"{i}. {name.strip()}")
        else:
            print("No names found.")
    
    # Respectful delay to avoid overwhelming the server
    time.sleep(2)

# Entry point
if __name__ == "__main__":
    main()
