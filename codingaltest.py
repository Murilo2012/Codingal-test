secret=50
guessnumber=int(input("What is your guess number?"))
i=1
while(i<6):
    print("It's not the number")
    if i== secret:
        print("Nice, it's the correct number")
if guessnumber + 5 <= secret:
    print("Ice cold")
elif guessnumber + 10 < secret: 
    print("Cold")
