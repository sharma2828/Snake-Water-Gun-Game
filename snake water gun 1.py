import random
print("MESSAGE FOR USER!!!---you can enter anything except snake water gun to quit the game")
L=["SNAKE","WATER","GUN"]
a=input("SNAKE WATER GUN ??: ")
b=(L[random.randint(0,2)])
print("COMPUTER INPUT:",b)
x=a.upper()
if x==b:
    print("DRAW")
elif x=="SNAKE" and b== "WATER":
    print("USER WINS")
elif x=="SNAKE" and b=="GUN":
    print("COMPUTER WINS")
elif x=="WATER" and b=="SNAKE":
    print("COMPUTER WINS")
elif x=="WATER" and b=="GUN":
    print("USER WINS")
elif x=="GUN" and b=="SNAKE":
    print("USER WINS")
elif x=="GUN" and b=="WATER":
    print("COMPUTER WINS")
else:
    print("INVALID INPUT-----GAME ENDED")   
    
 