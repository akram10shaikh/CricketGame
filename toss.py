import time,psllist,random
import action
from decision import Sel


# Teams in the tournament
teams =['india','australia','pakistan','new zealand']



# Toss and selecting the opponent
class Toss:

    # Displaying the selected team
    def display(self,t1):
        if t1 == 1:
            teams.remove('india')
            print()
            print("You selected team India")
            time.sleep(1)
            self.pteam = 'India'


        elif t1 == 2:
            teams.remove('australia')
            print()
            print("You selected team Australia")
            time.sleep(1)
            self.pteam = 'Australia'

        elif t1 == 3:
            teams.remove('pakistan')
            print()
            print("You selected team Pakistan")
            time.sleep(1)
            self.pteam = 'Pakistan'

        elif t1 == 4:
            teams.remove('new zealand')
            print()
            print("You selected team New zealand")
            time.sleep(1)
            self.pteam = 'New zealand'

    # Opponent Team Selection
    def opteam(self):
        opteam = random.choice(teams)
        self.oppt = None
        if opteam == 'india':
            print()
            print("Machine selected team India")
            time.sleep(1)
            self.oppt = 'India'

        elif opteam == 'australia':
            print()
            print("Machine selected team Australia")
            time.sleep(1)
            self.oppt = 'Australia'

        elif opteam == 'pakistan':
            print()
            print("Machine selected team Pakistan")
            time.sleep(1)
            self.oppt = 'Pakistan'

        elif opteam == 'new zealand':
            print()
            print("Machine selected team New zealand")
            time.sleep(1)
            self.oppt = 'New zealand'

    def bothteam(self):
        ts = Sel() # Calling Sel call for toss decision

        print()
        time.sleep(1)
        print("Match is between\n{} VS {} ".format(self.pteam,self.oppt))
        print()
        time.sleep(2)
        self.m,self.n= ts.toss_decision(self.pteam,self.oppt) # Result is store

        print("\nTeam list {}".format(self.pteam))
        time.sleep(2)
        if self.pteam == 'India':
            for i in psllist.india:
                print(i,)

        elif self.pteam == 'Australia':
            for i in psllist.australia:
                print(i,)

        elif self.pteam == 'Pakistan':
            for i in psllist.pakistan:
                print(i,)

        elif self.pteam == 'New zealand':
            for i in psllist.newzealand:
                print(i,)

        # Opponent team list
        print()
        time.sleep(2)
        print("\nTeam list {}".format(self.oppt))
        time.sleep(2)
        if self.oppt == 'India':
            for i in psllist.india:
                print(i, )

        elif self.oppt == 'Australia':
            for i in psllist.australia:
                print(i, )

        elif self.oppt == 'Pakistan':
            for i in psllist.pakistan:
                print(i, )

        elif self.oppt == 'New zealand':
            for i in psllist.newzealand:
                print(i, )


    def ac1(self):
        acti = action.Action()
        acti.rules()
        acti.act(self.m,self.n,self.pteam)
