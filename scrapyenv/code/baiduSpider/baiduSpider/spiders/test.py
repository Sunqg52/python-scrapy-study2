import requests
from bs4 import BeautifulSoup


headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
		'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
response = requests.get('https://baike.baidu.com/item/Python', headers=headers)
	
soup = BeautifulSoup(response.content,'lxml')
# print(soup)
url = response.url
title = soup.find(name='title').string
text = soup.find(name='meta', attrs={'name':'description'}).attrs['content']
lastUpdated = soup.find(name='meta', attrs={'itemprop':'dateUpdate'}).attrs['content']
		
print('URL: {}'.format(url))
print('title: {}'.format(title))
print('text: {}'.format(text))
print('last update: {}'.format(lastUpdated))