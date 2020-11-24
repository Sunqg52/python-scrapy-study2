from userInterface import * 

if __name__ == '__main__':
	massage = ''
	linklist = linkList()
	while massage != 'exit':
		key = user_choice()
		user(key,  linklist)
		massage = key
	print('bey')