import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
acsii = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))



if choice >= 3 or choice < 0:
    print("You Entered Innvalid Number.")
else:
    print("----" * 5)
    print(f"User choose:\n {acsii[choice]}")
    print("----" * 5)

    comChoice = random.randint(0,2)
    print(f"Computer choose:\n {acsii[comChoice]}")
    print("----" * 5)

    if choice == 0 and comChoice == 2:
        print("You Win!!!")
    elif comChoice == 0 and choice == 2:
        print("You Loose!!!")
    elif comChoice > choice:
        print("You Loose!!!")
    elif choice > comChoice:
        print("You Win!!!")
    elif choice == comChoice:
        print("Its a Draw.")
