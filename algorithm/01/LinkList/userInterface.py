from Node import Node
from linkList import linkList

def user_choice():
	key = input("\n请选择要执行的操作：1.新建单链表 2.插入结点 3.通过位置删除结点  4.通过数值查找结点 5.遍历输出\n")
	return key



def user(key, linklist):

	if key == '1':
		i = 1
		massage = ""
		while True:
			massage = input('\n请输入第{}个要存储的信息(输入\\q返回，exit退出):\t '.format(i))
			if massage == '\\q':
				break
			else:
				node = Node(massage)
				linklist.add_node(node)
				i += 1
	elif key == '2':
		index = input('请输入要插入的位置索引(输入q返回，exit退出)：')
		value = input('请输入要插入的值：')
		linklist.insert_node(index, value)
	elif key == '3':
		index = input('请选择要删除的位置索引(输入q返回，exit退出):')
		linklist.delete_node_byid(index)
	elif key == '4':
		value = input('请选择要查找的值(输入q返回，exit退出):')
		linklist.find_node(value)
	elif key == '5':
		linklist.print_link()







