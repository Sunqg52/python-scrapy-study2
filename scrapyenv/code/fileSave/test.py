from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?';
headers = {
	'Host': 'm.weibo.cn',
	'Referer': 'https://m.weibo.cn/u/2830678474',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
}

def get_json(since_id=None):
	params = {
		'uid': '2830678474',
		'luicode': '10000011',
		'lfid': '1076032830678474',
		'type': 'uid',
		'value': '2830678474',
		'containerid': '1076032830678474',
	}
	if since_id != None:
		params['since_id'] = since_id

	url = base_url + urlencode(params)

	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError as e:
		print('Error', e.args)


def get_sinceid(json):
	items = json.get('data').get('cardlistInfo')
	for since_id in items:
		if since_id:
			return items.get('since_id')

def get_page(json):
	if json:
		items = json.get('data').get('cards')
		dates = []
		for item in items:
			item = item.get('mblog')
			weibo = {}
			weibo['id'] = item.get('id')
			weibo['text'] = pq(item.get('text')).text()
			weibo['attitudes'] = item.get('attitudes_count')
			weibo['comments'] = item.get('comments_count')
			weibo['reposts'] = item.get('reposts_count')
			# yield weibo			# 迭代器
			dates.append(weibo)
	return dates

if __name__=='__main__':
	json = get_json()	
	print(type(json))
	# results = get_page(json)
	# for i in range(1,11):
	# 	since_id = get_sinceid(json)
	# 	json = get_json(since_id)
	# 	results.append(get_page(json))
	# 	for result in results:
	# 		print(result)