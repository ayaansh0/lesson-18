import random #importing random module 


while True:  #iterate loop
    user_action = input("enter a choice (rock , paper , scissors)")   #take input

    possible_actions = ["rock" , "paper" , "scissors"]
    #using random function
    computer_action = random.choice(possible_actions)
    print(f"\n Chose {user_action} , computer chose {computer_action} . ") #display both outputs what is selected by you and computer 



    #conditions to check who won the game 

    if user_action == computer_action:
        print("both players selected {user_action}. Cheating !! :( ")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock wins obvi ")
        else:
            print("paper wins cause rock is rock , LOSERRR ")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper wins cause rock is rock , LOSERRR")
        else:
            print("scissors cuts paper womp womp , LOSERR")
    elif user_action == "scissors":
        if computer_action == "paper":
            print ("scissors cuts , finally won ")

        else:
            print("rock smashes scissors . loserr")


#take input for playing again 
    play_again = input("play again ? Haha i'd win (y/n):")
    if play_again != "y":
      break 