import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

USERNAME = '17824237438'
PASSWORD = '5277gang.'

class CrackWeiboSlide():
	def __init__(self):

		self.url = 'http://passport.weibo.cn/signin/login'
		self.browser = webdriver.Chrome()
		self.wait = WebDriverWait(self.browser, 20)
		self.username = USERNAME 
		self.passwd = PASSWORD 

	def __del__(self):
		self.browser.close()

	def open(self):
		"""
		打开网页输入用户名密码并点击
		:return: None
		"""
		self.browser.get(self.url)
		username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
		passwd = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
		submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
		username.send_keys(self.username)
		passwd.send_keys(self.passwd)
		submit.click()

	def get_position(self):
		"""
		获取验证码位置
		:return: 验证码位置元组
		"""
		try:
			img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
		except TimeoutException:
			print('未出现验证码')
			self.open()

		time.sleep(2)
		location = img.location
		size = img.size
		top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'], size['width']
		return (top, bottom, left, right)

	def get_screenshot(self):
		"""
		获取验证码图片：
		: return: 图片对象
		"""

		screenshot = self.browser.get_screenshot_as_png()
		screenshot = Image.open(BytesIO(screenshot))
		return screenshot
	def get_image(self, name='captcha.png'):
		"""
		获取验证码图片
		:return : 图片对象
		"""
		top, bottom, left, right = self.get_position()
		print('验证码位置：', top, bottom, left, right)
		screenshot = self.get_screenshot()
		captcha = screenshot.crop(left, top, right, bottom)
		captcha.save(name)
		return captcha

	def main(self, name='captcha.png'):
		"""
		批量获取验证图片
		:return: 图片对象
		"""
		count = 0
		while True:
			self.open()
			self.get_image(str(count)+'.png')
			count += 1

if __name__ == '__main__':
	crack = CrackWeiboSlide()
	crack.main()