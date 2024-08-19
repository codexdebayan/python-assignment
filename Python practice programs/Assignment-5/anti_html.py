import sys
import requests
from bs4 import BeautifulSoup

def strip_html(url):
    try:
        # Fetching the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Parsing the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Stripping all HTML tags and getting the plain text
        text = soup.get_text()

        # Printing the plain text
        print(text)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python anti_html.py <URL>")
    else:
        url = sys.argv[1]
        strip_html(url)
