from bs4 import BeautifulSoup as bs
import requests as req

link = 'https://fitness.org.au/directory/reps/category/personal-trainer/1/14'

response = req.get(link)
soup = bs(response.content, 'html.parser')

name = soup.find('div', class_='search-item').find('a' class_='no-hover-underline').get('h2')

print(name)
