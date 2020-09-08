from random import randint
from time import sleep
from json import loads

Versions = ['v1.0.2', 'v2.5.1', 'v3.0.2', 'v4.3.0', 'v5.5.1'] #Very easy, easy, normal, hard, very hard

Dificulty = {'v1.0.2':"VeryEasy", 'v2.5.1':"Easy", 'v3.0.2':"Average", 'v4.3.0':"Hard", 'v5.5.1':"VeryHard"}

Version = Versions[randint(0, 4)]

Greting = """RobcoOS {0}
Password Required\n\n""".format(Version)

#Prints a greeting
for char in Greting:
    print(char, end='', flush=True)
    sleep(0.05)

#Check the word
def WordCheck(word, password):
    Similar = 0
    W = list(word)
    P = list(password)
    try:
        for i in range(0, len(password)):
            if W[i] == P[i]:
                Similar += 1
        return Similar
    except IndexError: 
        return 0

#In case of Sucsess
def Sucsess():
    print("Sucsess!")
    sleep(1)
    for i in range(25):
        print("\n", end='', flush=True)
        sleep(0.05)

#in case of Fail
def Fail():
    for i in range(25):
        print("\n", end='', flush=True)
        sleep(0.05)
    print(" "*30+"TERMINAL LOCKED")
    print(" "*23+"PLEASE CONTACT AN ADMINISTRATOR")
    print("\n"*12)

def Game():
    Attempts = 4

    with open('Data.json', 'r') as passwords:
        data=passwords.read()
    passwords = loads(data)

    Words = passwords[Dificulty[Version]] 

    Password = Words[randint(0, len(Words)-1)]

    while True:
        print("Attempts Remaining:{}".format(' *'*Attempts))
        print(Words) #18 lines
        guess = input(':').upper() #now it none case censative
        if WordCheck(guess, Password) == len(Password):
            Sucsess()
            break
        else:
            print("\n"*25)
            print(Greting)
            print("Entry denied {}".format(str(WordCheck(guess, Password))+'/'+str(len(Password))))
            Attempts -= 1
        
        if Attempts == 0:
            Fail()
            break

Game()