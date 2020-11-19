from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup

class ArticleSpider(CrawlSpider):
	name='article'
	allowed_domains = ['baike.baidu.com']	# 允许保留的链接 遍历包含'baike.baidu.com'的链接忽略外链
	start_urls = ['https://baike.baidu.com/item/Python']	# 起始链接
	rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',
		follow=True)]
	"""
	Rule 链接过滤规则
		LinkExtractor:必选参数，是一个LinkExtractor对象
		callback:用来解析网页内容的函数
		fllow: 将当前页面找到的链接添加到后面的抓取里
	"""
	def parse_items(self, response):	
		# 先提取url
		url = response.url	

		# scrapy 返回参数为tmlResponse类型，bs不接受故进行转换
		response = response.body.decode(encoding=response.encoding, errors='ignore')
		soup = BeautifulSoup(response,'lxml')
	
		title = soup.find(name='title').string
		text = soup.find(name='meta', attrs={'name':'description'}).attrs['content']
		lastUpdated = soup.find(name='meta', attrs={'itemprop':'dateUpdate'}).attrs['content']
				
		print('URL: {}'.format(url))
		print('title: {}'.format(title))
		print('text: {}'.format(text))
		print('last update: {}'.format(lastUpdated))