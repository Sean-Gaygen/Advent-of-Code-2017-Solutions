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
		self.weight = int(line.split('(')[1].split(')')[0])
		self.accumulative_weight = 0
		
		Program.all_programs[self.name] = self
	
	def build_family(self):
		
		if ' -> ' in self.line:
			
			for child in self.line.split(' -> ')[1].split(', '):
				
				self.children.append(Program.all_programs[child])
				Program.all_programs[child].parent = self.name
	
	def accumulate_weight(self):
		
		if self.children:
			
			for child in self.children:
				
				if not child.accumulative_weight:
					
					child.accumulate_weight()
				
				self.accumulative_weight += child.accumulative_weight
				#print(self.name, child.name, child.accumulative_weight)
			
			self.accumulative_weight += self.weight
		
		else:
			
			self.accumulative_weight = self.weight

	
Program.build_tree(data)  # TODO make this check programatic

for prog in Program.all_programs:
	
	if Program.all_programs[prog].name == 'ptshtrn':
		
		#print(Program.all_programs[prog].name, [i.name for i in Program.all_programs[prog].children])
		
		Program.all_programs[prog].accumulate_weight()
		
		for child in Program.all_programs[prog].children:
			
			print(child.name, child.weight, child.accumulative_weight)
			
