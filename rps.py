import random

choices= ["rock","paper","scissors"]
for i in range(0,3):
    computer=random.choice(choices)
    player= None
    while player not in choices:
        player=input("ROCK,PAPER OR SCISSORS ?: ").lower()

    computers=0
    players=0
    if player==computer:
        print("computer: ",computer)
        print("player: ",player)
        print("tie")
    elif player=="rock":
        if computer=="paper":
            print("computer: ", computer)
            print("player: ", player)
            print("COMPUTER WINS!! YOU LOOSE")
            computers=computers+1
        if computer=="scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!! COMPUTER LOST")
            players=players+1
    elif player=="paper":
        if computer=="scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("COMPUTER WINS!! YOU LOOSE")
            computers=computers+1
        if computer=="rock":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!! COMPUTER LOST")
            players=players+1
    elif player=="scissors":
        if computer=="rock":
            print("computer: ", computer)
            print("player: ", player)
            print("COMPUTER WINS!! YOU LOOSE")
            computers=computers+1
        if computer=="paper":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!! COMPUTER LOST")
            players=players+1
    print("Computer score: ",computers)
    print("your score: ",players)


