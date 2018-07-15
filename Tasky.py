import time
from TaskList import *
import os
import pickle

SAVE_LOC = 'tasky_save.txt'

#Tasky
def load():
	print('Welcome to Tasky')
	task_list = TaskList()
	try:
		file_obj = open(SAVE_LOC, 'rb')
		task_list = pickle.load(file_obj)
		print('Previous tasks loaded!')
	except():
		print('here')
		task_list.populate_list()
	return task_list

def main_screen(task_list):
	current_task = task_list.get_current_task()
	print('The current time is:')
	print('{0}'.format(time.strftime('%X')))
	print('Current Task: \n{0}'.format(current_task))
	print('Task List: {0}'.format(task_list.get_tasks()))
	
def add_task(task_list):
	task = str(input('Next Task (x to e(X)it):\n'))
	if (task.lower() == 'x'):
		return False
	elif (task.lower() == 'reset'):
		task_list.reset()
		return True
	elif (task.lower() == 'correct'):
		change = False
		task_change = str(input("Enter the corrected task:\n"))
		confirm = str(input('{0} will be replaced with {1}\nIs this correct? (y/n)?\n'.format(task_list.get_current_task(), task_change))).lower()
		if (confirm == 'y'):
			task_list.correct_task(task_change)
			change = True
		while (change == False or confirm == 'n'):
			task_change = str(input("Enter the corrected task:\n"))
			confirm = str(input('Is this correct? (y/n)?\n')).lower()
			if (confirm == 'y'):
				task_list.correct_task(task_change)
				change = True
		return True
		
	else:
		task_list.add_task(task)
		return True
		
def save(task_list):
	with open(SAVE_LOC, 'wb') as handle:
		pickle.dump(task_list, handle, -1)
	print('Tasky Saved!')

def main():
	task_list = load()
	main_screen(task_list)
	
	while (add_task(task_list)):
		print('\nTasky')
		main_screen(task_list)
	save(task_list)
	
main()