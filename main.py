import estado as funct

st = []
f = open ('archivo.txt','r') #Archivo que se va a leer
lines = f.read().split("\n") #Leer el archivo y colocar todos las lineas en un vector dividiendo por el caracter \n que es salto de linea
f.close() #Cierra el archivo 
states = lines[0].split(",") #Divide poniendolos en un vector
alphabet = lines[1].split(",") #Divide el alfabeto poniendolo en un vector
initial = lines[2] #Guarda el estado inicial en una variables
final = lines[3].split(",") #Guarda los estados iniciales en un vector

def getState(stat):
	for state in st:
		if state.getEstado() == stat:
			return state
	return null

def checkS(str):
	checkR(str,getState(initial),0,"")
	return

def checkR(str, state,cont,a):
	t=state.getTransitions()
	#print (state.getEstado())
	if cont<len(str):
		for x in range(0,len(t),2):
			#print(t[x], " == ",str[cont])
			if t[x] == str[cont] or t[x] == "&":
				checkR(str,getState(t[x+1]),cont+1,a+state.getEstado())
	else:
		if state.getFinal() == 1:
			print("Se acepta la cadena tomando el camino: ")
			for x in range(0,len(a)):
				print(a[x],"-> ",end="")
			print(state.getEstado())		
	return

#print("states: ",states)
#print("alphabet: ",alphabet)
#print("initial: ", initial)
#print("final: ",final)
#print(len(lines)-1) #tamano del vector se pone -1 porque al momento de leer se agrega un espacio vacio

transitions = []
for x in range(4, len(lines)-1):
    transitions.append(lines[x])

#print(transitions)

for state in states:
	st.append(funct.Estado(state))

for state in st:
	for transition in transitions:
		t = transition.split(",")
		#print(t[0]," == ", state.getEstado())
		if t[0] == state.getEstado():
			state.addTransition(t[1])

for state in st:
        for f in final:
                if state.getEstado() == f:
                        getState(f).setFinal()


#for state in st:
#	print("////////// ",state.getEstado()) 
#	state.printTransitions()

string = input("ingresa la cadena que quieres probar: ")

checkS(string)

