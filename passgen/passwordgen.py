import random
from termcolor import cprint
import sys

def main():
    generatepassword()

def generatepassword():
    print("Welcome to Password Generator, type in 'H' for help!")

    while True:
        in1 = input("How long do you want your password to be? ")
        helpandquit(in1) 
        if in1.isnumeric() == True:
             userinput = int(in1)
             if userinput <= 65536:
                gen(userinput)
             else:
                 cprint('\033[1m' + "ERROR: Number cannot be greater than 65,536.", 'red')
        else:        
             cprint('\033[1m' + "ERROR: PLEASE INSERT A NUMBER!", 'red')


def gen(x):
    wordlist = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*?' 
    password = ''
    for x in range(x):
        password += random.choice(wordlist)
    cprint('\033[1m' + password, 'green')

def helpandquit(x):
    message = "Hello, and welcome to my password generator, please insert a number for the length of your password, and let your computer generate it for you! To quit just press Q"
    quitcommand = {'Q', 'q', 'quit'}
    helpcommand = {'h', 'H', 'help'}
    if x in quitcommand:
        sys.exit()
    if x in helpcommand:
        cprint('\033[1m' + message, 'yellow')
    
main()
