
# 源代码实现
class queue(self):
	""" 创立容器"""
	def __init__(self):
		self.list=[]
	def enqueue(self, item):
		self.list.append(item)
	def dequeue(self):
		self.list.pop(0)
	def is_empty(self):
		return self.list==[]
	def size(self):
		return len(self.list)