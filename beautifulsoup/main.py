import requests
from bs4 import BeautifulSoup
 
# URL of the website you want to scrape
url = "https://tools.sars.gov.za/tradestatsportal/data_download.aspx"
# url = 'https://en.wikipedia.org/wiki/Machine_learning'
# url = 'https://www.neuralnine.com/'
 
# Send a GET request to the website
response = requests.get(url, verify= False)
 
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Example: Find all links on the page
    links = soup.find_all('a')
    for link in links:
        print(f" -------------------------\n{link.get('href')}")
else:
    print(f"Failed to retrieve the webpage:\n status: {response.status_code}")