import time,psllist,random,pickle

# Match summary Function
def match_summary():
    time.sleep(4)
    with open("batting1.data", "wb") as fg:
        pickle.dump(mc1, fg)
        fg.close()
    with open("bowling1.data", "wb") as bg:
        pickle.dump(bowler_lst1, bg)
        bg.close()

    print("          Match Summary       ")
    print("-" * 40)
    print("AUS {}/{} NZL {}/{}".format(score, wickets, score1, wickets1))
    print("-" * 40)

    print("NZL Batting")
    print("-" * 40)
    jd14 = 0
    with open("batting1.data", "rb") as fgh_h:
        dm = pickle.load(fgh_h)
        for id14 in range(1, len(dm), 2):
            print("{} : {} runs".format(dm[jd14], dm[id14]))
            jd14 = jd14 + 2
        fgh_h.close()
    time.sleep(1)
    print()
    print("-" * 40)
    print("AUS Bowling")
    print("-" * 40)
    mkd1 = 0
    with open("bowling1.data", "rb") as fghj:
        sm = pickle.load(fghj)
        for bz1 in range(1, len(sm), 2):
            print("{}  :  {}".format(sm[mkd1], sm[bz1]))
            mkd1 = mkd1 + 2
        fghj.close()
    print("-"*40)
    print()
    print("-"*40)
    print("AUS Batting")
    print("-" * 40)
    with open("batting.data", "rb") as fpp:
        jd3 = 0
        record_bat = pickle.load(fpp)
        for id3 in range(1, len(record_bat), 2):
            print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
            jd3 = jd3 + 2
        fpp.close()
        time.sleep(1)
        print()
    print("-" * 40)
    print("NZL Bowling")
    print("-" * 40)
    mkd3 = 0
    with open("bowling.data", "rb") as dpp:
        record_ball = pickle.load(dpp)
        for bz3 in range(1, len(record_ball), 2):
            print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
            mkd3 = mkd3 + 2
        dpp.close()
    print("-" * 40)
    time.sleep(10)


time.sleep(1)


global score
score = 0
wickets = 0
b1 = 0
b2 = 0

n1 = 0
n2 = 1
p1 = psllist.australia[n1]
p2 = psllist.australia[n2]
cr = p1
mc = []
bow = []
wcc = []
wc = 0
d1 = random.choice(psllist.newzealand[7:])
bdic = dict()
bowlerlst = []
print("AUS VS NZL")
print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
ball = 0
bowler_lst = [] # Bowlers and wickets list
zm = 0  # bowler list increment

for i in range(0, 2):
    bowler_lst.append(d1)
    zm = 0

    for j in range(1, 7):
        ball = ball + 1
        p1 = psllist.australia[n1]
        p2 = psllist.australia[n2]

        if cr == p1:
            print()
            print("Batsman: {} \nBowler: {}".format(p1, d1))
            time.sleep(1)
        else:
            print()
            print("Batsman: {} \nBowler: {}".format(p2, d1))
            time.sleep(1)
        print("\n------------")
        print("AUS VS NZL \n{}/{} \nOver {}.{} ".format(score, wickets, i, j))
        print("------------")
        print()
        sh = input("\nSelect the shot \nA->Risk S->Average D->Defensive: ").lower()
        time.sleep(1)

        if sh == 's':
            c1 = random.choice(psllist.shot[0:7])
            if cr == p1:
                print()
                print("Batsman: {} \nBowler: {}".format(p1, d1))
                time.sleep(1)
            else:
                print()
                print("Batsman: {} \nBowler: {}".format(p2, d1))
                time.sleep(1)
            if c1 == 1:
                score = score + 1
                if cr == p1:
                    b1 = b1 + 1
                    print()
                    print(psllist.one)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr = p2
                    time.sleep(1)

                else:
                    b2 = b2 + 1
                    print()
                    print(psllist.one)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr = p1
                    time.sleep(1)
            elif c1 == 3:
                score = score + 3
                if cr == p1:
                    b1 = b1 + 3
                    print()
                    print(psllist.three)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr = p2
                    time.sleep(1)

                else:
                    b2 = b2 + 3
                    print()
                    print(psllist.three)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr = p1
                    time.sleep(1)

            elif c1 == 2:
                score = score + 2
                if cr == p1:
                    b1 = b1 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b2 = b2 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)

        elif sh == 'a':
            c1 = random.choice(psllist.shot[8:])

            if cr == p1:
                print()
                print("Batsman: {} \nBowler: {}".format(p1, d1))
                time.sleep(1)
            else:
                print()
                print("Batsman: {} \nBowler: {}".format(p2, d1))
                time.sleep(1)
            if c1 == 4:
                score = score + 4
                if cr == p1:
                    b1 = b1 + 4
                    print(psllist.four)
                    time.sleep(1)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))
                    time.sleep(1)
                else:
                    b2 = b2 + 4
                    print(psllist.four)
                    time.sleep(1)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))

                    time.sleep(1)
            elif c1 == 6:
                score = score + 6
                if cr == p1:
                    b1 = b1 + 6
                    print(psllist.six)
                    time.sleep(1)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))
                    time.sleep(1)
                else:
                    b2 = b2 + 6
                    print(psllist.six)
                    time.sleep(1)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))
                    time.sleep(1)
            elif c1 == 2:
                score = score + 2
                if cr == p1:
                    b1 = b1 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b2 = b2 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c1, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)
            elif c1 == 0:

                if cr == p1:
                    print(psllist.out)
                    time.sleep(1)
                    print("Out {}".format(p1))
                    time.sleep(1)
                    n1 = n1 + 2
                    mc.append(p1)
                    mc.append(b1)

                    zm = zm + 1

                    print("{} runs \n{}".format(b1, random.choice(psllist.place)))
                    b1 = 0
                    wickets = wickets + 1
                    print()

                else:
                    print(psllist.out)
                    time.sleep(1)
                    print("Out {}".format(p2))
                    n2 = n2 + 2
                    time.sleep(1)
                    mc.append(p2)
                    mc.append(b2)

                    zm = zm + 1



                    print("{} runs \n{}".format(b2, random.choice(psllist.wic)))
                    b2 = 0
                    wickets = wickets + 1
                    print()

        else:
            print("\nDot ball")
            print()
            time.sleep(1)


    if ball == 12:
        if zm <= 0:
            zero = 0
            bowler_lst.append(zero)
        else:
            bowler_lst.append(zm)
    else:
        if zm <= 0:
            zero = 0
            bowler_lst.append(zero)
        else:
            bowler_lst.append(zm)


        # After the over is completed
        time.sleep(1)
        print()
        print("\nOver is completed \n\nAUS VS NZL {}/{} in {} Overs".format(score, wickets, i + 1))
        time.sleep(4)
        # Changing the strike of the Bastman
        if cr == p1:
            cr = p2
        else:
            cr = p1

        print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
        time.sleep(1)
        d1 = random.choice(psllist.newzealand[7:])
        print("\nNext Over")
        print("Bowler : {}".format(d1))
        time.sleep(2)
    # After the innings is completed add batsman in the dict
    if ball == 12:

        mc.append(p1)
        mc.append(b1)
        mc.append(p2)
        mc.append(b2)


# Score saving in files
with open("batting.data","wb") as fp:
    pickle.dump(mc,fp)
    fp.close()

with open("bowling.data","wb") as dp:
    pickle.dump(bowler_lst,dp)
    dp.close()
# Second Innings is started
time.sleep(3)
print(psllist.innings_over)
time.sleep(2)
print()
print("End of the first Innings ")
print("-"*40)
print("          Scorecard     ")
print("-"*40)
print("AUS Batting   {}/{}".format(score,wickets))
print("-"*40)
jd = 0
for id in range(1,len(mc),2):
    print("{} : {} runs" .format(mc[jd],mc[id]))
    jd = jd + 2
time.sleep(1)
print()
print("-"*40)
print("NZL Bowling")
print("-"*40)
mkd = 0
for bz in range(1,len(bowler_lst),2):
    print("{}  :  {}".format(bowler_lst[mkd],bowler_lst[bz]))
    mkd = mkd + 2

print()
print("-"*40)
print("Target {}".format(score+1))
print("-"*40)
time.sleep(10)



target = score + 1

bowler_list = psllist.australia[6:]
no_increment = 1
print()
time.sleep(2)
print("Second innings is stated ")
print()
print("Select the Bowler")
time.sleep(1)
for bowler_single in bowler_list:
    print("{}. {}".format(no_increment,bowler_single))
    no_increment = no_increment + 1
d11 = input("Input the Bowler name : ")
bowler_lst1 = []
bowler_lst1.append(d11)

time.sleep(1)

b11 = 0
b21 = 0

score1 = 0
wickets1 = 0

n11 = 0
n21= 1
p11 = psllist.newzealand[n11]
p21 = psllist.newzealand[n21]
cr1 = p11
mc1 = []
bow1 = []
wcc1 = []
wc1 = 0

num1 = 0



zm1 = 0 # For wicket record of the bowler
bowlerlst1 = []
print("AUS VS NZL")
print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

balls = 0
for ii in range(0, 2):
    mm1 = 1
    zm1 = 0
    for jj in range(1, 7):
        balls = balls + 1
        if cr1 == p11:
            print()
            print("Batsman: {} \nBowler: {}".format(p11, d11))
            time.sleep(1)
        else:
            print()
            print("Batsman: {} \nBowler: {}".format(p21, d11))
            time.sleep(1)

        p11 = psllist.newzealand[n11]
        p21 = psllist.newzealand[n21]
        print("\n------------")
        print("AUS VS NZL\n{}/{} Target {} \nOver {}.{} ".format(score1, wickets1,target, ii, jj))
        print("------------")
        sh1 = input("\nSelect the Ball Type \nA->Short Ball S->Good Line Ball D->Yorker Ball: ").lower()
        time.sleep(1)
        if sh1 == 's':
            c11 = random.choice(psllist.shot[0:7])
            if cr1 == p11:
                print()
                print("Batsman: {} \nBowler: {}".format(p11, d11))
                time.sleep(1)
            else:
                print()
                print("Batsman: {} \nBowler: {}".format(p21, d11))
                time.sleep(1)
            if c11 == 1:
                score1 = score1 + 1
                if cr1 == p11:
                    b11 = b11 + 1
                    print()
                    print(psllist.one)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr1 = p21
                    time.sleep(1)

                else:
                    b21 = b21 + 1
                    print()
                    print(psllist.one)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr1 = p11
                    time.sleep(1)
            elif c11 == 3:
                score1 = score1 + 3
                if cr1 == p11:
                    b11 = b11 + 3
                    print()
                    print(psllist.three)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr1 = p21
                    time.sleep(1)

                else:
                    b21 = b21 + 3
                    print()
                    print(psllist.three)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    cr1 = p11
                    time.sleep(1)

            elif c11 == 2:
                score1 = score1 + 2
                if cr1 == p11:
                    b11 = b11 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b21 = b21 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)

        elif sh1 == 'a':
            c11 = random.choice(psllist.shot[8:])

            if cr1 == p11:
                print()
                print("Batsman: {} \nBowler: {}".format(p11, d11))
                time.sleep(1)
            else:
                print()
                print("Batsman: {} \nBowler: {}".format(p21, d11))
                time.sleep(1)
            if c11 == 4:
                score1 = score1 + 4
                if cr1 == p11:
                    b11 = b11 + 4
                    print(psllist.four)
                    time.sleep(1)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))
                    time.sleep(1)
                else:
                    b21 = b21 + 4
                    print(psllist.four)
                    time.sleep(1)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))

                    time.sleep(1)
            elif c11 == 6:
                score1 = score1 + 6
                if cr1 == p11:
                    b11 = b11 + 6
                    print(psllist.six)
                    time.sleep(1)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))
                    time.sleep(1)
                else:
                    b21 = b21 + 6
                    print(psllist.six)
                    time.sleep(1)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[2:])))
                    time.sleep(1)
            elif c11 == 2:
                score1 = score1 + 2
                if cr1 == p11:
                    b11 = b11 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b21 = b21 + 2
                    print()
                    print(psllist.two)
                    print("{} runs {} {}".format(c11, random.choice(psllist.place),
                                                 random.choice(psllist.quality[0:2])))
                    time.sleep(1)
            elif c11 == 0:

                if cr1 == p11:
                    print(psllist.out)
                    time.sleep(1)
                    print("Out {}".format(p11))
                    time.sleep(1)
                    n11 = n11 + 2
                    mc1.append(p11)
                    mc1.append(b11)

                    zm1 = zm1 + 1

                    print("{} runs \n{}".format(b11, random.choice(psllist.place)))
                    b11 = 0
                    wickets1 = wickets1 + 1
                    print()

                else:
                    print(psllist.out)
                    time.sleep(1)
                    print("Out {}".format(p21))
                    n21 = n21 + 2
                    time.sleep(1)
                    mc1.append(p21)
                    mc1.append(b21)

                    zm1 = zm1 + 1



                    print("{} runs \n{}".format(b21, random.choice(psllist.wic)))
                    b21 = 0
                    wickets1 = wickets1 + 1
                    print()

        else:
            print("\nDot ball")
            print()
            time.sleep(1)



        # If target is chased excute this block
        if score1 >= target:
            num1 = 1
            time.sleep(2)
            mc1.append(p11)
            mc1.append(b11)
            mc1.append(p21)
            mc1.append(b21)
            print()
            print(psllist.won_the_match)
            print("Congrats!! \nTeam New Zealand\nYou Won the match\nWell Played")
            time.sleep(5)

            break

        # If the Over completed then the bowling team won the match
        if balls == 12:
            if score1 == score:
                print("\nMatch is tie\n\n Well played both the teams")
            else:
                num1 = 1
                mc1.append(p11)
                mc1.append(b11)
                mc1.append(p21)
                mc1.append(b21)

                print()
                print(psllist.won_the_match)
                time.sleep(1)
                print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                time.sleep(3)

                break

    # If the total is chased Exit the block
    if num1 == 1:
        if zm1 <= 0:
            zero1 = 0
            bowler_lst1.append(zero1)
            break

        else:
            bowler_lst1.append(zm1)
            break

    else:
        if zm1 <= 0:
            zero1 = 0
            bowler_lst1.append(zero1)

        else:
            bowler_lst1.append(zm1)

        # Else the loop continue
        time.sleep(1)
        print("\nOver is completed \nScore \nAUS VS NZL {}/{} in {} Overs\nTarget {}".format(score1, wickets1, ii + 1,target))
        # Changing the stick of the batsman
        if cr1 == p11:
            cr1 = p21
        else:
            cr1 = p11
        print()
        print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
        print()

        time.sleep(3)

        # Selecting the Bowler to ball next over
        print()
        print("Bowler list")
        time.sleep(2)
        no_increment1 = 1
        for bowler_single1 in bowler_list:
            print("{}. {}".format(no_increment1, bowler_single1))
            no_increment1 = no_increment1 + 1
        d11 = input("Input the Bowler Name: ")
        bowler_lst1.append(d11)

match_summary()