import time
from TaskList import *
import os
#Tasky
def load():
	print('Welcome to Tasky')
	task_list = TaskList()
	try:
		open_data = []
		file = open('tasky_save.txt', 'r')
		in_data = file.readlines()
		task_list.set_count(in_data.pop(-1))
		for line in in_data:
			task_list.add_task(line[:-1])
		print('Previous tasks loaded!')
	except():
		open_data = task_list.populate_list()
	return task_list

def main_screen(task_list):
	current_task = task_list.get_current_task()
	print('The current time is:')
	print('{0}'.format(time.strftime('%X')))
	print('Current Task: \n{0}'.format(current_task))
	print('Task List: {0}'.format(task_list.get_tasks()))
	
def add_task(task_list):
	task = str(input('Next Task (x to exit):\n'))
	if (task.lower() != 'x'):
		task_list.add_task(task)
		return True
	else:
		return False
def save(task_list):
	file = open('tasky_save.txt', 'w')
	for task_element in task_list.save():
		file.write(str(task_element) + "\n")

def main():
	task_list = load()
	main_screen(task_list)
	
	while (add_task(task_list)):
		print('\nTasky')
		main_screen(task_list)
	
	save(task_list)
	
main()