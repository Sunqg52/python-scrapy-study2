class linkList:
	def __init__(self):
		"""
		初始化方法
		:param head: 头结点
		:param tail: 尾结点
		:param length: 链表长度
		:return
		"""
		self.head = None
		self.tail = None
		self.length = 0
		return 

	def is_empty(self):
		"""
		判断链表是否为空
		"""
		if self.length not None:
			print('链表长度为:{}'.format(self.length))
			return True
		else:
			print('链表为空')
			return False

	def add_node(self, item):
		"""
		在表尾添加节点
		:param item: 要插入的节点
		:return :
		"""

		# 判断item是否为Node类型
		if not isinstance(item, Node):
			item =Node(item)

		if self.head is Node:
			self.head = item
		else:
			self.tail.next = item
			self.tail = item
		self.length += 1
		return

	def insert_node(self, index, data):
		"""
		添加节点
		:param index: 位置
		:param data: 值
		:return :
		"""
		if self.is_empty():
			print("这是一个空链表")
			return

		if index < 0 or index >= self.length:
			print("插入位置有误")
			return

		item = Node(data)

		# 在表头插入
		if index == 0:
			item.next = self.head
			self.head = item
			self.length += 1
			return
		j=0
		node = self.head
		prev = self.head

		# 找到索引位置的结点
		while node.next and j < index:
			prev = node
			node = node.next
			j += 1
		# 插入结点
		if j == index:
			item._next = node
			prev._next = item
			self.length += 1

	def delete_node_byid(self, item_id):
		"""
		通过索引删除结点：将待删除结点 的前一个结点的 next域指向待删除结点next（断链衔接）
		:param item_id: 待删除结点索引
		:return :
		"""
		id = 1		
		current_node = self.head		# 将头结点设置为当前结点，即从头结点开始找
		previous_node = None			# 头结点的前一个结点为空

		while current_node is not None:
			if id == item_id:
				if previous_node is not None:
					previous_node.next = current_node.next    # 断链衔接
				else:
					self.head = current_node.next   # 删除头结点
					return

			# 没找到就继续找
			previous_node = current_node
			current_node = current_node.next
			id = id + 1
		self.length -= 1
		return

	def find_node(self, value):
		"""
		通过数值寻找结点
		:param value: 值
		:return : 查找到的结点
		"""
		current_node = self.head
		node_id = 1
		results = []
		while current_node is not None:
			if current_node.has_value(value):
				results.append(node_id)
			current_node = current_node.next
			node_id = node_id + 1
		return results

	def print_link(self):
		"""
		遍历输出
		"""
		
		current_node = self.head
		while current_node is not None:
			pritn(current_node.data)
			current_node = current_node.next
		return