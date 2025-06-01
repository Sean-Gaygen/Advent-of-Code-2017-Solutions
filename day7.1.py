with open('day7.txt') as f:
	data = [i.strip() for i in f.readlines()]


class Program:
	
	all_programs = {}
	
	def build_tree(raw_data):
		
		for prog in raw_data:
			
			Program(prog)
		
		for current_program in Program.all_programs:
			
			Program.all_programs[current_program].build_family()
	
	def __init__(self, line):
		
		self.line = line
		self.parent = None
		self.children = []
		self.name = line.split(' ')[0]
		
		Program.all_programs[self.name] = self
	
	def build_family(self):
		
		if ' -> ' in self.line:
			
			for child in self.line.split(' -> ')[1].split(', '):
				
				self.children.append(Program.all_programs[child])
				Program.all_programs[child].parent = self.name
	
Program.build_tree(data)

for prog in Program.all_programs:
	
	if not Program.all_programs[prog].parent:
		
		print(Program.all_programs[prog].name)
		break