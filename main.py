from functions import getState, check, readFile, printResult

readFile('automaton.txt')
string = input("Enter the string you want to try: ")
check(string)
printResult()
