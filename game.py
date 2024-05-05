import logo, action
import time
from toss import Toss

# Object for Toss Class
toss = Toss()

print(logo.cricket)
print("Welcome to the Cricket Game")
time.sleep(2)
ch1 = input("Do you want to Play Cricket (yes/no) :").lower()
if ch1 == 'yes':
    # Team selection
    while True:
        try:
            time.sleep(2)
            print()
            print("Welcome to the JB cricket game. \nYou can play JB cricket game with 4 teams. \nChoose your team to start the JB cricket match.")
            print()
            time.sleep(2)
            t1 = int(input("Select the team from 1 to 4\n1.India\n2.Australia\n3.Pakistan\n4.New zealand\nYou Choice : "))
            break
        except:
            print("Only numbers are allowed from 1 to 4")
            time.sleep(2)
            print("Try Again")
            time.sleep(2)
            print()
    # Toss and Team selection
    toss.display(t1)

    # Opponent Team selection
    toss.opteam()

    # Both team
    toss.bothteam()

    toss.ac1()