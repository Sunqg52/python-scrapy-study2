from queue import Queue


"""
# 使用Python自带的队列：头尾双口管道，一边进一边出
put()在队尾添加元素
get()在队头取出元素，返回队头元素
empty():判断队列是否为空
full():判断队列是否已满
qsize():队列当前长度
"""
q = Queue(maxsize=0)
q.put(1)
q.put(2)

q.get()
print('长度', q.qsize())
print('判空', q.empty())
print('判满', q.full())