import estado as funct

####################global variables############
st = []
states = []
alphabet = []
initial = []
final = []
transitions = []
results = []

def getState(stat):
	for state in st:
		if state.getEstado() == stat:
			return state
	return

def checkS(str):
	checkR(str,getState(initial),0,"",255)
	return

def checkR(str, state,cont,a,ttl):
	t=state.getTransitions()
	for x in range(0,len(t),2):
		if t[x] == "&":
			checkR(str,getState(t[x+1]),cont,a+state.getEstado(),ttl-1)

	if cont<len(str) and ttl>0:
		for x in range(0,len(t),2):
			if t[x] == str[cont]:
				checkR(str,getState(t[x+1]),cont+1,a+state.getEstado(),ttl-1)
	else:
		if state.getFinal() == 1:
			global results
			results.append(a+state.getEstado())
	return

def printResult():
	if len(results) != 0:
		print("Se acepta la cadena")
		print("Se encontraron ",len(results), " caminos diferentes")
		print("El primer camino encontrado es: ")
		for x in range(0,len(results[0])-1):
			print(results[0][x],"-> ",end="")
		print(results[0][len(results[0])-1])
	else:
		print("No se acepta la cadena")
	return

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
		st.append(funct.Estado(state))

	for state in st:
		for transition in transitions:
			t = transition.split(",")
			if t[0] == state.getEstado():
				state.addTransition(t[1])

	for state in st:
		for f in final:
			if state.getEstado() == f:
				getState(f).setFinal()
