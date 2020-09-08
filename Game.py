#Attempts Remaining: * * * *
from random import randint
from time import sleep

Dificulty = ['v1.0.2', 'v2.5.1', 'v3.0.2', 'v4.3.0', 'V5.5.1'] #Very easy, easy, normal, hard, very hard

GameDif = Dificulty[randint(0, 4)]

Greting = """RobcoOS {0}
Password Required\n""".format(GameDif)

#Prints a greeting
for char in Greting:
    print(char, end='', flush=True)
    sleep(0.05)