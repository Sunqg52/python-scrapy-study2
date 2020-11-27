from urllib.parse import urlencode
from urllib.request import urlretrieve
import requests
import re
import os
"""
1. 根据链接获取json信息
2. 根据返回的json信息提取出图片的objURL
4. 对提取出的objURL解码转换
4. 根据objURL下载图片
"""

def get_json():
	"""根据链接获取json信息"""

	baseUrl = 'https://image.baidu.com/search/index?'
	headers = {
		'Host':'image.baidu.com',
		'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&word=%E7%81%AB%E5%BD%B1',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
	}
	params = {
		'tn': 'resultjson_com',
		'logid': '10981796017892247737',
		'ipn': 'rj',
		'ct': '201326592',
		'is': '',
		'fp': 'result',
		'queryWord': '火影',		# 关键字 可自行更改
		'cl': '2',
		'lm': '-1',
		'ie': 'utf-8',
		'oe': 'utf-8',
		'adpicid': '',
		'st': '-1',
		'z': '',
		'ic': '0',
		'hd': '',
		'latest': '',
		'copyright': '',
		'word': '火影',		# 关键字 可自行更改
		's': '',
		'se':'' ,
		'tab': '',
		'width': '',
		'height': '',
		'face': '0',
		'istype': '2',
		'qc': '',
		'nc': '1',
		'fr': '',
		'expermode': '',
		'force': '',
		'pn': '30',		# 本页图片数量 需要的可以自行修改
		'rn': '30',			
		'gsm': '3c',
		'1606372009928': '',
	}

	url = baseUrl + urlencode(params)
	print(url)
	try:
		# response = requests.get(url=url, headers=headers, allow_redirects=False)
		response = requests.get(url, headers=headers, allow_redirects=False).json()
		# if response.status_code == 200:
		return response
	except requests.ConnectionError as e:
		print(e.args)

def get_objUrl(pageInfo):

	if pageInfo.get('data'):
		urls = []
		data = pageInfo.get('data')
		for info in data:
			if info.get('objURL'):
				url = info.get('objURL')
				urls.append(url)
				print(url)
		return urls
	else:
		print('json获取失败')

def  img_decode(url):
    res = ''
    c = ['_z2C$q', '_z&e3B', 'AzdH3F']
    decode = {
    	'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', 
    	'2':'g', 'i':'h', 't':'i', '3':'j', 'h':'k', 's':'l', 
    	'4':'m', 'g':'n', '5':'o', 'r':'p', 'q':'q', '6':'r', 
    	'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1', 
    	'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 
    	'b':'8', 'l':'9', 'a':'0', '_z2C$q':':', '_z&e3B':'.',
    	 'AzdH3F':'/',
    	}
    if(url==None or 'http' in url):
        return url
    else:
        j= url
        for m in c:
            j=j.replace(m,decode[m])
        for char in j:
            if re.match('^[a-w\d]+$',char):
                char = decode[char]
            res= res+char
        return res

def download_img(url, count):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			urlretrieve(url,'img{}.jpg'.format(count))

	except requests.ConnectionError as e:
		print('保存失败！ Error: ', e.args)

def main(urllist, count=0):
	
	for url in urlList:
		url = img_decode(url)
		download_img(url, count)
		count += 1

if __name__ == '__main__':
	pageInfo = get_json()
	urlList = get_objUrl(pageInfo)
	main(urlList)
