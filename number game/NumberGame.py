import random #importing module 
playing = True #initialise 
number = str(random.randint(10,20))  #random in-built function 

print("I will generate a number from 0 to 21, and you have to guess the number one digit at a time " )
print("The game ends when you get 1 win")

#iterate loop till the condition is true

while playing:
    guess = input("Guess")
    if number == guess:
        print("you win the game")
        print("it is what it is ")
        break 

    else:
        print("Wrong !!  Boo ")
