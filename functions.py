import classes as classes
import copy

####################global variables############
st = []
states = []
alphabet = []
initial = []
final = []
transitions = []
results = []


####################get a state#################
def getState(stat):
	for state in st:
		if state.getState() == stat:
			return state
	return

####################check functions##############
def check(str):
	a = []
	checkR(str,getState(initial),0,a,255)#String to check, state to analize, string counter, path, time to live
	return

def checkR(str, state, cont, a, ttl):#cadena, estado a analizar, contador de la palabra, camino, time to live
	t=state.getTransitions()
	for x in range(0,len(t),2):
		if t[x] == "&":
			b = copy.copy(a)
			b.append(state.getState())
			checkR(str,getState(t[x+1]),cont,b,ttl-1)

	if cont<len(str) and ttl>0:
		for x in range(0,len(t),2):
			if t[x] == str[cont]:
				b = copy.copy(a)
				b.append(state.getState())
				checkR(str,getState(t[x+1]),cont+1,b,ttl-1)
	else:
		if state.getFinal() == 1:
			global results
			a.append(state.getState())
			results.append(a)
	return

######################Print the result########
def printResult():
	if len(results) != 0:
		print("\nThe string is accepted")
		print("\nWith the path: ")
		for x in range(0,len(results[0])-1):
			print(results[0][x],"-> ",end="")
		print(results[0][len(results[0])-1])
		print("\nTotal paths: ",len(results),"\n")
	else:
		print("\nThe string is rejected")
	return

########################Read the file#########
def readFile(file):

	global st, states, alphabet, initial, final, transitions

	f = open (file,'r') #Archivo que se va a leer
	lines = f.read().split("\n") #Leer el archivo y colocar todos las lineas en un vector dividiendo por el caracter \n que es salto de linea
	f.close() #Cierra el archivo

	states = lines[0].split(",") #Divide poniendolos en un vector
	alphabet = lines[1].split(",") #Divide el alfabeto poniendolo en un vector
	initial = lines[2] #Guarda el estado inicial en una variables
	final = lines[3].split(",") #Guarda los estados iniciales en un vector

	for x in range(4, len(lines)-1):
		transitions.append(lines[x])

	for state in states:
		st.append(classes.State(state))

	for state in st:
		for transition in transitions:
			t = transition.split(",")
			if t[0] == state.getState():
				state.addTransition(t[1])

	for state in st:
		for f in final:
			if state.getState() == f:
				getState(f).setFinal()
