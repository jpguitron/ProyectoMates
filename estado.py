class Transition:
	def __init__(self,inp,state): #constructor
		self.inp = inp
		self.state = state
	def getInp(self):
		return self.inp
	def getState(self):
		return self.state

class Estado:		

	def __init__(self,estado):
		self.estado = estado
		self.transitions = []
		self.final = 0		

	def addTransition(self, trans):
		t = trans.split(":")
		transition = Transition(t[0],t[1])
		self.transitions.append(transition)
	
	def setFinal(self):
		self.final = 1

	def getFinal(self):
		return self.final
		
	def getEstado(self):
		return self.estado
	
	def getTransitions(self):
		t = []
		for transition in self.transitions:
			t.append(transition.getInp())
			t.append(transition.getState())
		return t  	
		
	def printTransitions(self):
		for transition in self.transitions:
			print(transition.getInp(), "->",transition.getState())	
