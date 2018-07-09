import time
#Tasky
def load():
	try:
		open_data = file('tasky_save.txt', r)
	except():
		open_data = populate_list()
		
def populate_list():
	task_list = []
	for i in range(3):
		task_list[i] = input("Enter task {0}:".format(i + 1))
		if (task_list[i] == ""):
			print("No input detected!")
			task_list[i] = input("Enter task {0}:".format(i + 1))

def intro():
	print('Welcome to Tasky')
	print('The current time is:')
	print('{0}'.format(time.strftime('%X %x %Z')))

def main():
	intro()

main()