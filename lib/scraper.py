import requests
from bs4 import BeautifulSoup

# Set up headers and make a GET request to the website
headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html.content, "html.parser")

# Find all <a> tags (links) on the page
links = soup.find_all('a')

# Print out each link's URL (href attribute)
with open("scraped_links.txt", "w") as file:
    for link in links:
        href = link.get('href')
        if href:
            file.write(href + "\n")

print("Scraping complete! Links have been saved to 'scraped_links.txt'")
