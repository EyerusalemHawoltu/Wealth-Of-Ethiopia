# Web Scraping Project: Richest Ethiopians

## Overview
This project is designed to scrape data from the webpage listing the 15 richest Ethiopians and their successful companies. Utilizing Python's `requests` library to handle HTTP requests and `BeautifulSoup` for parsing HTML, this script retrieves and displays the names of the richest individuals in Ethiopia.

## Features
- **Website Scraping**: The script fetches the content of the specified URL, which contains the relevant data about the richest Ethiopians.
- **Error Handling**: Implements retry logic to handle HTTP errors gracefully, including a specific response for rate limiting (HTTP 429).
- **Data Extraction**: Extracts the names of the richest individuals by parsing the HTML content and filtering the relevant headings.
- **User-Friendly Output**: Displays the names in a numbered list format for easy readability.

## Code Structure

### Imports:
- `requests`: For sending HTTP requests.
- `time`: To manage delays between requests.
- `BeautifulSoup` from `bs4`: For parsing HTML content.

### Configuration:
- The target URL is defined as a constant at the beginning of the script.
- Custom headers are used to simulate a browser visit and avoid detection by web servers.

### Functions:
- `scrape_website(url, retries)`: Sends a GET request to the specified URL and returns a parsed HTML object. It includes retry logic for handling errors.
- `extract_richest_people(soup)`: Takes a BeautifulSoup object, extracts the relevant names from `<h2>` tags, and returns a list of the richest individuals.

### Main Execution:
- The script begins execution in the `main()` function, which orchestrates the scraping and data extraction processes.

## Usage
Simply run the script to initiate the web scraping process. The names of the 15 richest Ethiopians will be printed to the console.
