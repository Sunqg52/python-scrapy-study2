from os import listdir

class ModelMate():
	def __init__():

	def detect_image(self, image):
		"""
		匹配图片
		:param image: 图片
		:return: 拖动顺序
		"""
		for template_name in listdir(TEMPLATES_FOLDER):
			print('正在匹配', template_name)
			template = Image.open(TEMPLATES_FOLDER + template_name)
			if self.same_image(image, template):
				# 返回顺序
				numbers = [int(number) for number in list(template_name.split('.')[0])]
				print('拖动顺序', numbers)
				return numbers

	def is_pixel_equal(self, image1, image2, x, y):
		"""
		判断两个图片像素是否相同
		:param image1: 图片1
		:param image2: 图片2
		:param x: 位置x
		:param y: 位置y
		"""

		# 提取两个图片像素点
		pixel1 = image1.load()[x,y]
		piexl2 = image2.load()[x,y]
		threshold = 20
		if abs(piexl1[0] - piexl2[0]) < threshold and \
			abs(piexl1[1] - piexl2[1]) < threshold and abs(piexl1[2] - piexl2[2]) < threshold
			return True
		else:
			return False

	def same_image(self, image, template):
		"""
		识别相似的验证码
		:param image: 待识别的验证码
		:param template: 模版
		:return :
		"""

		# 相似度阈值
		threshold = 0.99
		count = 0
		for x in range(image.width):
			for y in range(image.height):
				# 判断像素是否相同
				if self.is_pixel_equal(image, template, x, y):
					count += 1
		result = float(count) / (image.width * image.height)
		if result > threshold:
			print('成功匹配')
			return True
		return False