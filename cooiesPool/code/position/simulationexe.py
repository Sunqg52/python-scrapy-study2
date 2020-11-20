
class SimulationExe():
	def __init__(self):

	def move(self, numbers):
		"""
		根据顺序进行拖动
		:param numbers: 拖动顺序数字
		:return: 
		"""
		circles = self.browser.find_elements_by_css_selector('.patt-warp .patt-circ')
		dx = dy = 0
		for index in range(4):
			circle = circles[numbers[index] - 1]
			# 如果是第一次循环
			if index == 0:
				# 点击第一个按点
				ActionChains(self.browser) \
					.move_to_element_with.offset(circle, circle.size['width'] / 2, circle.size['height'] / 2) \
					.click_and_hold().perform()

			#如果是最后一次循环
			if index == 3:
				# 松开鼠标
				ActionChains(self.browser).release().perform()
			else:
				#计算下一次偏移
				dx = cricle[numbers[index + 1] - 1].location['x'] - circle.location['x']
				dy = cricle[numbers[index + 1] - 1].location['y'] - circle.location['y']