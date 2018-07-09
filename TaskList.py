import json

class TaskList:
	def __init__(self):
		self.count = 0
		self.taskList = ['' for i in range(3)]
		
	def __str__(self):
		return 'Task List: {0}\nCount: {1}'.format(self.taskList, self.count) 
		
	def populate_list(self):
		for i in range(3):
			self.taskList  += ['']
			self.taskList[i] = str(input("Enter task {0}:".format(i + 1)))
			while (self.taskList[i] == ""):
				print("No input detected!")
				self.taskList[i] = str(input("Enter task {0}:".format(i + 1)))
				
	def inc_count(self):
		self.count = (self.count + 1) % 3
		
	def set_count(self, value):
		self.count = int(value) % 3
		
	def get_count(self):
		return self.count
	
	def add_task(self, task, index = 'default'):
		if (index == 'default'):
			index = self.count % 3
		self.taskList[index] = task
		self.inc_count()
		
	def add_new_task(self, task):
		self.add_task(task)
		self.inc_count()
		
	def get_current_task(self):
		curr_index = self.count % 3
		return self.taskList[curr_index]
		
	def get_tasks(self):
		return self.taskList
		
	def save(self):
		print(self.taskList + [self.count])
		return self.taskList + [self.count]
		
class JsonSerializable(object):
	def toJson(self):
		return json.dumps(self.__dict__)
		
	def __repr__(self):
		return self.toJson()
		
class FileItem(JsonSerializable):
    def __init__(self, fname):
        self.fname = fname