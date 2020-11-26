import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = ''

def getAbsoluteURL(baseUrl, source):
	"""规范化链接"""
	if source.startswith('http://www.'):	# startswith() 判断是否以指定字符串开头
		url = 'http://{}'.format(source[11:])
	elif source.startswith('http://'):
		url = source
	elif source.startswith('www.'):
		url = source[4:]
		url = 'http://{}'.format(source)
	else:
		url = '{}/{}'.format(baseUrl, source)
	if baseUrl not in url:
		return None

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	path = absoluteUrl.replace('www.', '')
	path = path.replace(baseUrl, '')
	path = downloadDirectory + path
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)
	return path

html = urlopen('http://www.pathonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True)

for downloaded in downloadList:
	fileUrl = getAbsoluteURL(baseUrl, download['src'])
	if fileUrl is not None:
		print(fileUrl)
		# urlretrieve 将远程数据下载到本地
		urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))  