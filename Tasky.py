import time
from TaskList import *
import os
#Tasky
def load():
	task_list = TaskList()
	try:
		open_data = []
		task_index = 0
		in_data = open('tasky_save.txt', 'r').read().split()
		print(in_data)
		task_list.set_count(in_data.pop(-1))
		for line in in_data:
			task_list.add_task(line, task_index)
			task_index += 1
		print(task_list)
	except():
		open_data = task_list.populate_list()
	return task_list

def intro(task_list):
	current_task = task_list.get_current_task()

	print('Welcome to Tasky')
	print('The current time is:')
	print('{0}'.format(time.strftime('%X')))
	print('Current Task: {0}'.format(current_task))

def main():
	task_list = load()
	intro(task_list)

main()