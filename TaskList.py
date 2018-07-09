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
		self.count += 1
		
	def set_count(self, value):
		self.count = int(value)
		
	def get_count(self):
		self.count = self.taskList.pop(-1)
	
	def add_task(self, task, index):
		self.taskList[index] = task
		
	def get_current_task(self):
		curr_index = self.count % 3
		return self.taskList[curr_index]