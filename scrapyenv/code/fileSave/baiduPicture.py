import os
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

class baiduPicture:
	def __init__(self, keyword):
		self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'.format(keyword)

	def get_Link(self):
		"""获取图片链接"""

		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
		}
		response = requests.get(self.url, headers=headers)

		soup = BeautifulSoup(response.content, 'lxml')
		pictureLinks = []
		links = soup.find_all('li') # , {'class':'imgitem'}
		# print(type(links))
		for link in links:
			print(link)
			pictureLinks.append(link.attrs['data-objurl'])
		return pictureLinks

	def download(self):
		links = self.get_Link()
		num = 1
		for link in links:
			if link is not None:
				print(url)
				urlretrieve(link, 'download/{}'.format(num))
				num += 1

