import random, psllist
import time
import pickle

class Bowling:
    def bowl_first(self,y,x):

        # India VS Pakistan First bowling India
        if y == "India" and x == "Pakistan":
            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("PAK {}/{} IND {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("IND Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("PAK Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("PAK Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("IND Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("IND VS PAK")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.india[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.pakistan[n11]
            p21 = psllist.pakistan[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("IND VS PAK")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.pakistan[n11]
                    p21 = psllist.pakistan[n21]
                    print("\n------------")
                    print("IND VS PAK\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nIND VS PAK {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("PAK Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("IND Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.india[n1]
            p2 = psllist.india[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.pakistan[7:])
            bdic = dict()
            bowlerlst = []
            print("IND VS PAK")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.india[n1]
                    p2 = psllist.india[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("IND VS PAK\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam India\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam Pakistan\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nIND VS PAK {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.pakistan[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # India VS Australia First bowling India
        if y == "India" and x == "Australia":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("AUS {}/{} IND {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("IND Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
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
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("AUS Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("IND Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("IND VS AUS")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.india[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.australia[n11]
            p21 = psllist.australia[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("IND VS AUS")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.australia[n11]
                    p21 = psllist.australia[n21]
                    print("\n------------")
                    print("IND VS AUS\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nIND VS AUS {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("AUS Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("IND Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.india[n1]
            p2 = psllist.india[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.australia[7:])
            bdic = dict()
            bowlerlst = []
            print("IND VS AUS")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.india[n1]
                    p2 = psllist.india[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("IND VS AUS\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam India\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nIND VS AUS {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.australia[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # India VS New zealand first bowling India
        if y == "India" and x == "New zealand":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("NZL {}/{} IND {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("IND Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("NZL Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("NZL Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("IND Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("IND VS NZL")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.india[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.newzealand[n11]
            p21 = psllist.newzealand[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("IND VS NZL")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
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
                    print("IND VS NZL\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nIND VS NZL {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("NZL Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("IND Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.india[n1]
            p2 = psllist.india[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.newzealand[7:])
            bdic = dict()
            bowlerlst = []
            print("IND VS NZL")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.india[n1]
                    p2 = psllist.india[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("IND VS NZL\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam India\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam New zealand\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nIND VS NZL {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.newzealand[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()



        # Pakistan vs India first bowling Pakistan
        if y == "Pakistan" and x == "India":
            import time, random
            import psllist
            import pickle

            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("IND {}/{} PAK {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("PAK Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("IND Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("IND Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("PAK Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("PAK VS IND")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.pakistan[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.india[n11]
            p21 = psllist.india[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("PAK VS IND")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.india[n11]
                    p21 = psllist.india[n21]
                    print("\n------------")
                    print("PAK VS IND\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nPAK VS IND {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("IND Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("PAK Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.pakistan[n1]
            p2 = psllist.pakistan[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.india[7:])
            bdic = dict()
            bowlerlst = []
            print("PAK VS IND")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.pakistan[n1]
                    p2 = psllist.pakistan[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("PAK VS IND\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam Pakistan\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam India\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nPAK VS IND {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.india[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # Pakistan vs Australia first bowling Pakistan
        if y == "Pakistan" and x == "Australia":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("AUS {}/{} PAK {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("PAK Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
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
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("AUS Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("PAK Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("PAK VS AUS")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.pakistan[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.australia[n11]
            p21 = psllist.australia[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("PAK VS AUS")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.australia[n11]
                    p21 = psllist.australia[n21]
                    print("\n------------")
                    print("PAK VS AUS\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nPAK VS AUS {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("AUS Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("PAK Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.pakistan[n1]
            p2 = psllist.pakistan[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.australia[7:])
            bdic = dict()
            bowlerlst = []
            print("PAK VS AUS")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.pakistan[n1]
                    p2 = psllist.pakistan[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("PAK VS AUS\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam Pakistan\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nPAK VS AUS {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.australia[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # Pakistan vs New zealand first bowling Pakistan
        if y == "Pakistan" and x == "New zealand":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("NZL {}/{} PAK {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("PAK Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("NZL Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("NZL Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("PAK Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("PAK VS NZL")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.pakistan[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.newzealand[n11]
            p21 = psllist.newzealand[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("PAK VS NZL")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
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
                    print("PAK VS NZL\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nPAK VS NZL {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("NZL Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("PAK Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.pakistan[n1]
            p2 = psllist.pakistan[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.newzealand[7:])
            bdic = dict()
            bowlerlst = []
            print("PAK VS NZL")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.pakistan[n1]
                    p2 = psllist.pakistan[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("PAK VS NZL\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam Pakistan\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam New zealand\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nPAK VS NZL {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.newzealand[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()


        # Australia vs India first bowling Australia
        if y == "Australia" and x == "India":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("IND {}/{} AUS {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("AUS Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("IND Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("IND Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("AUS Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("AUS VS IND")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.australia[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.india[n11]
            p21 = psllist.india[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("AUS VS IND")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.india[n11]
                    p21 = psllist.india[n21]
                    print("\n------------")
                    print("AUS VS IND\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nAUS VS IND {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("IND Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("AUS Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

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
            d1 = random.choice(psllist.india[7:])
            bdic = dict()
            bowlerlst = []
            print("AUS VS IND")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
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
                    print("AUS VS IND\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam India\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nAUS VS IND {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.india[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # Australia vs Pakistan first bowling Australia
        if y == "Australia" and x == "Pakistan":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("PAK {}/{} AUS {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("AUS Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("PAK Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("PAK Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("AUS Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("AUS VS PAK")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.australia[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.pakistan[n11]
            p21 = psllist.pakistan[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("AUS VS PAK")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.pakistan[n11]
                    p21 = psllist.pakistan[n21]
                    print("\n------------")
                    print("AUS VS PAK\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nAUS VS IND {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("IND Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("AUS Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

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
            d1 = random.choice(psllist.pakistan[7:])
            bdic = dict()
            bowlerlst = []
            print("AUS VS PAK")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
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
                    print("AUS VS PAK\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam Pakistan\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nAUS VS PAK {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.pakistan[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # Australia vs New zealand first bowling Australia
        if y == "Australia" and x == "New zealand":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("NZl {}/{} AUS {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("AUS Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("NZl Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("NZl Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("AUS Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("AUS VS NZl")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.australia[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.newzealand[n11]
            p21 = psllist.newzealand[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("AUS VS NZl")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
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
                    print("AUS VS NZl\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nAUS VS NZl {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("NZl Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("AUS Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

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
            print("AUS VS NZl")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
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
                    print("AUS VS NZl\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam New Zealand\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nAUS VS NZl {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.newzealand[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()


        # New zealand vs India first bowling New zealand
        if y == "New zealand" and x == "India":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("IND {}/{} NZl {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("NZl Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("IND Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("IND Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("NZl Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("NZl VS IND")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.newzealand[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.india[n11]
            p21 = psllist.india[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("NZl VS IND")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.india[n11]
                    p21 = psllist.india[n21]
                    print("\n------------")
                    print("NZl VS IND\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nNZl VS IND {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("IND Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("NZl Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.newzealand[n1]
            p2 = psllist.newzealand[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.india[7:])
            bdic = dict()
            bowlerlst = []
            print("NZl VS IND")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.newzealand[n1]
                    p2 = psllist.newzealand[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("NZl VS IND\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam New Zealand\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam India\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nNZl VS IND {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.india[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # New zealand vs India first bowling New zealand
        if y == "New zealand" and x == "Pakistan":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("PAK {}/{} NZl {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("NZl Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
                    dm = pickle.load(fgh_h)
                    for id14 in range(1, len(dm), 2):
                        print("{} : {} runs".format(dm[jd14], dm[id14]))
                        jd14 = jd14 + 2
                    fgh_h.close()
                time.sleep(1)
                print()
                print("-" * 40)
                print("PAK Bowling")
                print("-" * 40)
                mkd1 = 0
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("PAK Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("NZl Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("NZl VS PAK")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.newzealand[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.pakistan[n11]
            p21 = psllist.pakistan[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("NZl VS PAK")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.pakistan[n11]
                    p21 = psllist.pakistan[n21]
                    print("\n------------")
                    print("NZl VS PAK\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nNZl VS PAK {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("PAK Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("NZl Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.newzealand[n1]
            p2 = psllist.newzealand[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.pakistan[7:])
            bdic = dict()
            bowlerlst = []
            print("NZl VS PAK")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.newzealand[n1]
                    p2 = psllist.newzealand[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("NZl VS PAK\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam New Zealand\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam Pakistan\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nNZl VS PAK {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.pakistan[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()

        # New zealand vs India first bowling New zealand
        if y == "New zealand" and x == "Australia":

            import time, random
            import psllist
            import pickle
            # Match summary Function
            def match_summary():
                time.sleep(4)
                with open("batting.data", "wb") as fg:
                    pickle.dump(mc, fg)
                    fg.close()
                with open("bowling.data", "wb") as bg:
                    pickle.dump(bowler_lst, bg)
                    bg.close()

                print("          Match Summary       ")
                print("-" * 40)
                print("AUS {}/{} NZl {}/{}".format(score1, wickets1, score, wickets))
                print("-" * 40)

                print("NZl Batting")
                print("-" * 40)
                jd14 = 0
                with open("batting.data", "rb") as fgh_h:
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
                with open("bowling.data", "rb") as fghj:
                    sm = pickle.load(fghj)
                    for bz1 in range(1, len(sm), 2):
                        print("{}  :  {}".format(sm[mkd1], sm[bz1]))
                        mkd1 = mkd1 + 2
                    fghj.close()
                print("-" * 40)
                print()
                print("-" * 40)
                print("AUS Batting")
                print("-" * 40)
                with open("batting1.data", "rb") as fpp:
                    jd3 = 0
                    record_bat = pickle.load(fpp)
                    for id3 in range(1, len(record_bat), 2):
                        print("{} : {} runs".format(record_bat[jd3], record_bat[id3]))
                        jd3 = jd3 + 2
                    fpp.close()
                    time.sleep(1)
                    print()
                print("-" * 40)
                print("NZl Bowling")
                print("-" * 40)
                mkd3 = 0
                with open("bowling1.data", "rb") as dpp:
                    record_ball = pickle.load(dpp)
                    for bz3 in range(1, len(record_ball), 2):
                        print("{}  :  {}".format(record_ball[mkd3], record_ball[bz3]))
                        mkd3 = mkd3 + 2
                    dpp.close()
                print("-" * 40)
                time.sleep(10)

            #      Main Function
            print("NZl VS AUS")
            time.sleep(1)
            print("\nBowler are ready to ball")
            time.sleep(1)
            bowler_list = psllist.newzealand[6:]
            no_increment1 = 1
            print()
            print("Select the Bowler")
            time.sleep(1)
            for bowler_single1 in bowler_list:
                print("{}. {}".format(no_increment1, bowler_single1))
                no_increment1 = no_increment1 + 1
            d11 = input("Input the Bowler name : ")
            bowler_lst1 = []
            bowler_lst1.append(d11)

            time.sleep(1)

            b11 = 0
            b21 = 0

            score1 = 0
            wickets1 = 0

            n11 = 0
            n21 = 1
            p11 = psllist.australia[n11]
            p21 = psllist.australia[n21]
            cr1 = p11
            mc1 = []
            bow1 = []
            wcc1 = []
            wc1 = 0

            num1 = 0

            zm1 = 0  # For wicket record of the bowler
            bowlerlst1 = []
            print("NZl VS AUS")
            print("{} and {} is Batting\n{} Bowling".format(p11, p21, d11))

            balls1 = 0
            for ii in range(0, 2):
                mm1 = 1
                zm1 = 0
                for jj in range(1, 7):
                    balls1 = balls1 + 1
                    if cr1 == p11:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p11, d11))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p21, d11))
                        time.sleep(1)

                    p11 = psllist.australia[n11]
                    p21 = psllist.australia[n21]
                    print("\n------------")
                    print("NZl VS AUS\n{}/{}  \nOver {}.{} ".format(score1, wickets1, ii, jj))
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

                if balls1 == 12:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)
                else:
                    if zm1 <= 0:
                        zero1 = 0
                        bowler_lst1.append(zero1)
                    else:
                        bowler_lst1.append(zm1)

                    # After the over is completed
                    time.sleep(1)
                    print()
                    print("\nOver is completed \n\nNZl VS AUS {}/{} in {} Overs".format(score1, wickets1, ii + 1))
                    time.sleep(4)
                    # Changing the strike of the Bastman
                    if cr1 == p11:
                        cr1 = p21
                    else:
                        cr1 = p11

                    print("{} : {} runs\n{} : {}".format(p11, b11, p21, b21))
                    time.sleep(1)
                    print()
                    print("Next over\nBowlers list")
                    time.sleep(2)
                    no_increment = 1
                    for bowler_single in bowler_list:
                        print("{}. {}".format(no_increment, bowler_single))
                        no_increment = no_increment + 1
                    d11 = input("Input the Bowler Name: ")
                    bowler_lst1.append(d11)

                # After the innings is completed add batsman in the list
                if balls1 == 12:
                    mc1.append(p11)
                    mc1.append(b11)
                    mc1.append(p21)
                    mc1.append(b21)

            # Score saving in files
            with open("batting1.data", "wb") as fp1:
                pickle.dump(mc1, fp1)
                fp1.close()

            with open("bowling1.data", "wb") as dp1:
                pickle.dump(bowler_lst1, dp1)
                dp1.close()
            # Second Innings is started
            time.sleep(3)
            print(psllist.innings_over)
            time.sleep(2)
            print()
            print("End of the first Innings ")
            print("-" * 40)
            print("          Scorecard     ")
            print("-" * 40)
            print("AUS Batting   {}/{}".format(score1, wickets1))
            print("-" * 40)
            jd1 = 0
            for id1 in range(1, len(mc1), 2):
                print("{} : {} runs".format(mc1[jd1], mc1[id1]))
                jd1 = jd1 + 2
            time.sleep(1)
            print()
            print("-" * 40)
            print("NZl Bowling")
            print("-" * 40)
            mkd1 = 0
            for bz1 in range(1, len(bowler_lst1), 2):
                print("{}  :  {}".format(bowler_lst1[mkd1], bowler_lst1[bz1]))
                mkd1 = mkd1 + 2

            print()
            print("-" * 40)
            print("Target {}".format(score1 + 1))
            print("-" * 40)
            time.sleep(10)

            # Second Innings is started
            target = score1 + 1
            time.sleep(2)
            print("Second innings is started ")

            time.sleep(1)

            score = 0
            wickets = 0
            b1 = 0
            b2 = 0

            n1 = 0
            n2 = 1
            p1 = psllist.newzealand[n1]
            p2 = psllist.newzealand[n2]
            cr = p1
            mc = []
            bow = []
            wcc = []
            wc = 0
            d1 = random.choice(psllist.australia[7:])
            bdic = dict()
            bowlerlst = []
            print("NZl VS AUS")
            print("{} and {} is Batting\n{} Bowler".format(p1, p2, d1))
            ball = 0
            bowler_lst = []  # Bowlers and wickets list
            zm = 0  # bowler list increment

            for i in range(0, 2):
                bowler_lst.append(d1)
                zm = 0

                for j in range(1, 7):
                    ball = ball + 1
                    p1 = psllist.newzealand[n1]
                    p2 = psllist.newzealand[n2]

                    if cr == p1:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p1, d1))
                        time.sleep(1)
                    else:
                        print()
                        print("Batsman: {} \nBowler: {}".format(p2, d1))
                        time.sleep(1)
                    print("\n------------")
                    print("NZl VS AUS\n{}/{} Target {} \nOver {}.{} ".format(score, wickets, target, i, j))
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

                        # If target is chased excute this block
                    if score >= target:
                        num1 = 1
                        time.sleep(2)
                        mc.append(p1)
                        mc.append(b1)
                        mc.append(p2)
                        mc.append(b2)
                        print()
                        print(psllist.won_the_match)
                        print("Congrats!! \nTeam New Zealand\nYou Won the match\nWell Played")
                        time.sleep(5)

                        break

                        # If the Over completed then the bowling team won the match
                    if ball == 12:
                        if score == score1:
                            print("\nMatch is tie\n\n Well played both the teams")
                        else:
                            num1 = 1
                            mc.append(p1)
                            mc.append(b1)
                            mc.append(p2)
                            mc.append(b2)

                            print()
                            print(psllist.won_the_match)
                            time.sleep(1)
                            print("Congrats!! \nTeam Australia\nYou Won the match\nWell Played")
                            time.sleep(3)

                            break

                    # If the total is chased Exit the block
                if num1 == 1:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)
                        break

                    else:
                        bowler_lst.append(zm)
                        break

                else:
                    if zm <= 0:
                        zero = 0
                        bowler_lst.append(zero)

                    else:
                        bowler_lst.append(zm)

                    # Else the loop continue
                    time.sleep(1)
                    print(
                        "\nOver is completed \nScore \nNZl VS AUS {}/{} in {} Overs\nTarget {}".format(score1, wickets1,
                                                                                                       ii + 1,
                                                                                                       target))
                    # Changing the stick of the batsman
                    if cr == p1:
                        cr = p2
                    else:
                        cr = p1
                    print()
                    print("{} : {} runs\n{} : {}".format(p1, b1, p2, b2))
                    print()

                    time.sleep(3)

                    # Selecting the Bowler to ball next over
                    print()
                    d1 = random.choice(psllist.australia[7:])
                    print("\nNext Over")
                    print("Bowler : {}".format(d1))

            match_summary()