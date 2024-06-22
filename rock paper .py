import random # type: ignore
choices = ["rock","paper", "scissor"]
computer = random.choice(choices)
player = None
while player not in choices:
    player = input("Please select and option from rock, paper, scissors")
if player == computer:
    print("Player option : "+player)
    print("computer option : "+computer)
elif player == "rock":
    if computer == "paper":
        print("Player option : "+player)
        print("computer option : "+computer)
        print("Oh no computer wins nice try")
    if computer == "scissor":
        print("nice you won")
        print("Player option : "+player)
        print("computer option : "+computer)
elif player == "paper":
    if computer == "rock":
        print("nice you won")
        print("Player option : "+player)
        print("computer option : "+computer)
    if computer == "scissor":
        print("sorry mate you lost")
        print("Player option : "+player)
        print("computer option : "+computer)
elif player =="scissor":
    if computer == "rock":
        print("oh no you lost")
        print("Player option : "+player)
        print("computer option : "+computer)
    if computer  == "paper":
        print("ggs you won")
        print("Player option : "+player)
        print("computer option : "+computer)