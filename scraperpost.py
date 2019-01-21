import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def parse_post(soup):
    return {
        'subject': soup.select('h1.headline a')[0].text,
        # extract text out of all child elements
        'body': soup.select('div.entry-content')[0].get_text(separator='\n'),
        'timestamp': soup.select('article time')[0].get('datetime'),
    }

url = 'https://publicpool.kinja.com/subject-remarks-by-president-trump-at-the-american-far-1831763583'
post_soup = get_soup(url)
post = parse_post(post_soup)

#can set these particular variables
print(post['subject'])
print(post['timestamp'])
print(post['body'])