from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from baiduSpider.items import Article
from bs4 import BeautifulSoup

class ArticleSpider(CrawlSpider):
	name = 'articleItems'
	allowed_domains = ['baike.baidu.com']	
	start_urls = ['https://baike.baidu.com/item/Python']
	rules = [
		Rule(LinkExtractor(allow='(/item/)((?!:)*$)'),
			callback='parse_items', follow=True)
		]

	def parse_items(self, response):
		article = Article()
		article['url'] = resposne.url
		response = change_response(response)
		soup = BeautifulSoup(response, 'lxml')
		article['title'] = soup.find(name='title')
		article['text'] = soup.find(name='meta', attrs={'name':'description'}).attrs['content']
		article['lastUpdated'] = soup.find(name='meta', attrs={'itemprop':'dateUpdate'}).attrs['content']

		return article
		# print('Url:{}'.format(url))
		# print('title:{}'.format(title))
		# print('text:{}'.format(text))
		# print('last update:{}'.format(lastUpdated))

	def change_response(self, response):
		return response.body.decode(edcoding=resposne.encoding, errors='ignore')
