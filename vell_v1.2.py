import webbrowser as web
from time import sleep as offset
import time
import random
global time
time = time.ctime()
##--------------------------------#
##Developed by Jose Barranco
##--------------------------------#
global runtime
runtime = 0
global undefined_runtime
undefined_runtime = 1
print "<-- This program was developed by Jose Barranco -->"
print "Welcome, initializing..."
offset(3)
print "This program started running on: " + time
offset(2)
print "Hello, my name is Vell"
global query
while True:
    query = str(raw_input("> "))
    break
##try:
##    f2 = open("greetings.txt")
##    greetings = f2.read().splitlines()
##    f2.close
##except IOError:
##    print "Couldn't find file"
##    
##try:
##    f = open("greet_complements.txt")
##    greet_complements = f.read().splitlines()
##    f.close()
##except IOError:
##    print "Couldn't find file"
##
##def greet(sentence):
##        greet = sentence + random.choice(greet_complements)
##        return greet
##print(greet(random.choice(greetings)))

if query.startswith("search"):
        
    global end_of_line
    end_of_line = query[5:22]
    def com_address(string):
        if query.startswith("search"):
            web.open(query[10:])
    com_address(query)
        
if query.startswith("Search"):
    end_of_line = query[5:22]
    def com_address_2(string):
        if query.startswith("Search"):
            web.open(query[10:])
    com_address_2(query)
    
try:    
    if query.startswith("open"):
        def find_address():
            address = query.index("www")
            if query[address:].endswith(".com"):
                address_found = query[address:]
                web.open(address_found)
        find_address()

    elif query.startswith("Open"):
     def find_address_2():
        address = query.index("www")
        if query[address:].endswith(".com"):
            address_found = query[address:]
            web.open(address_found)
     find_address_2()
except ValueError:
    addup = "www."
    addup_complete = query[5:5] + addup + query[5:]
    web.open(addup_complete)
    
    
   
finish = raw_input("Press 'Enter' to exit..")
quit()
##Integrated calculator module
calc_word = "calculator"
if calc_word or calc_word.capitalize() in query:
        
    print("Write 1 for Addition, 2 for Substraction, 3 for Multiplication, 4 for Division")
    operation = raw_input("> ")
    if "1" in operation:
        print "Addition Operation Selected"
        number_1 = int(raw_input("> "))
        print "Plus"
        number_2 = int(raw_input("> "))
        answer = number_1 + number_2
        print "Equals -> " + str(answer) 
    elif "2" in operation:
        print "Substraction Operation Selected"
        number_1 = int(raw_input("> "))
        print "Minus"
        number_2 = int(raw_input("> "))
        answer = number_1 - number_2
        print "Equals -> " + str(answer)
    elif "3" in operation:
        print "Multiplication Operation Selected"
        number_1 = int(raw_input("> "))
        print "Multiplied by:"
        number_2 = int(raw_input("> "))
        answer = number_1 * number_2
        print "Equals -> " + str(answer)
    elif "4" in operation:
        print "Division Operation Selected"
        number_1 = int(raw_input("> "))
        print "Divided by:"
        number_2 = int(raw_input("> "))
        answer = number_1 / number_2
        print "Equals -> " + str(answer)
                       
                       
                       
    

        
