import random,time
coin = ['h','t']
ba = ['bat','ball']
coins = ['Head','Tail']


# Toss
class Sel:
    def toss_decision(self,x,y):


        while True:
            ts = input("Match Refree is with the coin\nWho is calling \nAre you calling (yes/no) ").lower()
            time.sleep(2)
            if ts == 'yes':
                ts1 = input("\nok \nHead or Tail (H/T)").lower() # Taking from user Head or tail
                c2 = random.choice(coin)
                if ts1 == c2: # If user won the toss print
                    print("Congrats!\n{}\nYou won the Toss".format(x))
                    time.sleep(2)
                    s2 = input("Chose Batting or Bowling (Bat/Ball)) ").lower()
                    if s2 == 'bat':
                        time.sleep(2)
                        print("{} decided to Bat first ".format(x))
                        final = x
                        looser = y
                        break

                    elif s2 == 'ball':
                        time.sleep(2)
                        print("{} decided to Field first ".format(x))
                        final = y
                        looser = x
                        break

                    else:
                        print("Try Gain")
                else: # else user lose the toss
                    print("{} lose the toss".format(x))
                    opp3 = random.choice(ba)
                    if opp3 == 'bat':
                        time.sleep(2)
                        print("{} is Selected to Bat first ".format(y))
                        final = y
                        looser = x
                        break


                    else:
                        time.sleep(1)
                        print("{} is selected to Field first".format(y))
                        final = x
                        looser = y
                        break



            elif ts == 'no':
                op1 = random.choice(coins) #For machine toss
                print("\nHead or Tail\nOpponent {} selected {}".format(y,op1))
                time.sleep(1)
                ts2 = random.choice(coins) # Umpire coins spinning
                opp2 = random.choice(ba) # Machine is selecting bat or ball
                if op1 == ts2:
                    time.sleep(2)
                    print("\nBad luck!\nToss won by {}".format(y))
                    time.sleep(2)
                    if opp2 =='bat':
                        print("{} decided to Bat first ".format(y))
                        time.sleep(1)
                        final = y
                        looser = x
                        break
                    else:
                        print("{} decided to Field first ".format(y))
                        time.sleep(1)
                        final = x
                        looser = y
                        break


                else:
                    print("\n{} lose the toss ".format(y))
                    time.sleep(1)
                    s3 = input("Chose Batting or Bowling (Bat/Ball)) ").lower()
                    if s3 == 'bat':
                        time.sleep(2)
                        print("{} decided to Bat first ".format(x))
                        final = x
                        looser = y
                        break

                    elif s3 == 'ball':
                        time.sleep(2)
                        print("{} decided to Field first ".format(x))
                        final = y
                        looser = x
                        break

                    else:
                        print("Try Gain")

            else:
                print("\nTry again\n")

        return final,looser
