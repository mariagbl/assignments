import json
import requests
#takes html and makes it easy to provide structure for python analysis
from bs4 import BeautifulSoup
from pprint import pprint as pp

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_index(soup):
    post_elements = soup.select('.post-wrapper article')
    posts = []
    for el in post_elements:
        #looping through elements
        #href is an attribute, you can get it with .get 
        post = {
            'id': el.get('id'),
            'subject': el.select('h1 a')[0].text,
            'link': el.select('h1 a')[0].get('href')
        }
        posts.append(post)
    return posts

url = 'https://kinja.com/poolreports?startTime=1492123377164'

#empty array
posts = []
#nfinte loop
while True:
    print(url)
    index_soup = get_soup(url)
    #gets soup and parses it 
    posts += parse_index(index_soup)

    # check if load more button exists
    button = index_soup.select('.load-more__button a')
    if button:
        # get url from the load more button
        url = "https://publicpool.kinja.com/" + button[0].get('href')
    else:
        # exit the loop if we reached the last page
        break

with open('index.json', 'w') as f:
    json.dump(posts, f)