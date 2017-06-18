import webbrowser as web
from time import sleep as offset
import time
import random
global time
time = time.ctime()
#--------------------------------#
#Developed by Jose Barranco
#--------------------------------#
print "<-- This program was developed by Jose Barranco -->"
global undefined_runtime
undefined_runtime = 1
global runtime
runtime = 0
print "Welcome, initializing..."
offset(3)
print "This program started running on: " + time
offset(2)
print "Hello, my name is Vell"
global query
query = str(raw_input("> "))
global needed_file
needed_file = " which is a necessary file for this program to run."
global cannot
cannot = "Cannot find file: "
global no_file
no_file = "Please contact Jose Barranco if issues with program files persist."
global greet_file
greet_file = "greetings.txt"
user_greets_1 = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
user_greets_2 = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
user_greets_3 = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
user_greets_4 = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
user_greets_5 = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
user_greets_6 = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
global user_greets
try:
    f = open(greet_file)
    greetings = f.read().splitlines()
    f.close()
    if random.choice(user_greets_1) in query:
        print random.choice(greetings)
    elif random.choice(user_greets_2) in query:
        print random.choice(greetings)
    elif random.choice(user_greets_3) in query:
        print random.choice(greetings)
    elif random.choice(user_greets_4) in query:
        print random.choice(greetings)
    elif random.choice(user_greets_5) in query:
        print random.choice(greetings)
    elif random.choice(user_greets_6) in query:
        print random.choice(greetings)
except IOError:
    print cannot + greet_file + needed_file
    offset(1)
    print no_file
    offset(2)
    no_file_exit = str(raw_input("Press any key to exit."))
    exit()
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
    
    
elif query.startswith("open"):
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
finish = raw_input("Press any key to exit..")
confirm = raw_input("Sure you want to exit? Press any key to yes")

