from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
# import json
# from urllib.request import ProxyHandler, build_opener
# from dataChange import MyEncoder

def get_json():
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
		'queryWord': '火影',
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
		'word': '火影',
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
		'pn': 60,
		'rn': '30',
		'gsm': '3c',
		'1606372009928': '',
	}

	# proxy = '27.43.187.21:9999'
	# proxy_handler = ProxyHandler({
	# 	'http':'http://' + proxy,
	# 	'https': 'https://' + proxy
	# 	})
	# opener = build_opener(proxy_handler)

	url = baseUrl + urlencode(params)
	print(url)
	try:
		# response = requests.get(url=url, headers=headers, allow_redirects=False)
		response = requests.get(url, headers=headers, allow_redirects=False).json()
		# if response.status_code == 200:
		return response
	except requests.ConnectionError as e:
		print(e.args)

def get_objUrl(json):
	if json.get('data'):
		urls = []
		for data in json.get('data'):
			# print(data)
			urls.append(data.get('objURL'))
			return urls
	else:
		print('json获取失败')

if __name__ == '__main__':
	pageInfo = get_json()
	print(type(pageInfo))
	# pageInfo = str(pageInfo)
	# if isinstance(pageInfo, bytes):
	# 	pageInfo=str(pageInfo, encoding='utf-8')

	# with open('pageInfo2.json', 'w') as f:
	# 	json.dumps(pageInfo,indent=4)
	
	urlList = get_objUrl(pageInfo)
	for url in urlList:
		print(url)
	# urlList = get_json()