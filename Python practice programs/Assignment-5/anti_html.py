import sys
import requests
from bs4 import BeautifulSoup

def strip_html(url):
    try:
        # Fetching the HTML content
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.get_text()

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