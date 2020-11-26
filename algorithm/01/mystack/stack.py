class Stack:
	def __init__(self):
		"""创建空栈"""
		self.data=[]

	def __len__(self):
		return len(self.data)

	def isempty(self):
		return len(self.data)==0

	def push(self, value):
		self.data.append(d)

	def gettop(self):
		if self.isempty():
			return "stack is empty"
		return self.data[-1]

	def pop(self):
		if self.isempty():
			return "stack is empty"
		return self.data.pop()
