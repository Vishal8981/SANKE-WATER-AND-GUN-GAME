import random
list=["s", "w" ,"g"]
n=1
n1=int(input("Enter how many times you want to play the game "))
y=0
c=0
while(n<=n1):
    b = input("Enter the choice i.e. s ,w or g \n")
    rand = random.choice(list)
    if (rand==b):
        print("tie the game")
    elif(b=="s" and rand=="w"):
        y=y+1
        print ("you win 1 point")
        print("human point=",y)
        print("computer point=",c)
    elif (b == "s" and rand == "g"):
        c = c + 1
        print("computer win 1 point")
        print("human point=", y)
        print("computer point=", c)
    elif(b=="w" and rand=="s"):
        c = c + 1
        print("computer win 1 point")
        print("human point=", y)
        print("computer point=", c)
    elif(b=="w" and rand=="g"):
        y = y + 1
        print("you win 1 point")
        print("human point=", y)
        print("computer point=", c)
    elif(b=="g" and rand=="s"):
        y = y + 1
        print("you win 1 point")
        print("human point=", y)
        print("computer point=", c)
    elif(b=="g" and rand=="w"):
        c = c + 1
        print("computer win 1 point")
        print(f"human point= {y} computer point ={c}")

    n=n+1
print("game over hoga bhai")
if(y==c):
    print("tie")
elif(y>c):
    print("you win the game and computer loss")
else:
    print("you loss the game and computer win")
print(f"your point is {y} and computer point is {c}")
