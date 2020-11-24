class Node:
	def __init__(self,data=''):
		self.data = data
		self.next = None
		return 

	def has_value(self, value):
		if self.data == value:
			return True
		else:
			False