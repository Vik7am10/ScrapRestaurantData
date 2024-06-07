import requests
from bs4 import BeautifulSoup
import openai
import time
import csv


# URL of the Yelp search results page
url = "https://www.yelp.ca/search?find_desc=Restaurants&find_loc={Waterloo%2C+ON}"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find(class_='list__09f24__ynIEd')

#Loading into CSV
f = open('yelp3.csv', 'w')
writer = csv.writer(f)
writer.writerow(['name', 'rate', 'reviews', 'styles'])

for d in div.contents[2:12]:
    name = d.find(class_='y-css-12ly5yx').text
    rate = d.find(class_='y-css-jf9frv').text
    reviews = d.find('span', class_='y-css-wfbtsu').text
    styles = d.find(class_='y-css-1cn4gbs').text
    writer.writerow([name, rate, reviews, styles])
f.close()
