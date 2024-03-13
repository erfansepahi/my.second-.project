import random

dice = 0
while dice != 6:
    dice = random.randint(1 , 6)
    print("number obtained form rolling the dice:" , dice)
if dice == 6:
    print("congratulations! rolling the dice again")
input("press enter to exit ")
