import random,psllist,time

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
print("Ind VS Pak")
print("{} and {} is Batting\n{} Bowler".format(p1,p2,d1))


for i in range(0,2):
    mm = 1
    for j in range(1,7):
        p1 = psllist.india[n1]
        p2 = psllist.india[n2]
        print("\n------------")
        print("Ind vs Pak \n{}/{} \nOver {}.{} ".format(score, wickets, i,j))
        print("------------")
        sh = input("\nSelect the shot \nS->Average A->Risk D->Defensive: ").lower()
        time.sleep(1)

        if sh == 's':
            c1 = random.choice(psllist.shot[0:7])
            if cr == p1:
                print("Batsman: {} \nBowler: {}".format(p1, d1))
                time.sleep(1)
            else:
                print("Batsman: {} \nBowler: {}".format(p2, d1))
                time.sleep(1)
            if c1 == 1:
                score = score + 1
                if cr == p1:
                    b1 = b1 + 1
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    cr = p2
                    time.sleep(1)

                else:
                    b2 = b2 + 1
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    cr = p1
                    time.sleep(1)
            elif c1 == 3:
                score = score + 3
                if cr == p1:
                    b1 = b1 + 3
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    cr = p2
                    time.sleep(1)

                else:
                    b2 = b2 + 3
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    cr = p1
                    time.sleep(1)

            elif c1 == 2:
                score = score + 2
                if cr == p1:
                    b1 = b1 + 2
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b2 = b2 + 2
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    time.sleep(1)

        elif sh == 'a':
            c1 = random.choice(psllist.shot[8:])
            if cr == p1:
                print("Batsman: {} \nBowler: {}".format(p1, d1))
                time.sleep(1)
            else:
                print("Batsman: {} \nBowler: {}".format(p2, d1))
                time.sleep(1)
            if c1 == 4:
                score = score + 4
                if cr == p1:
                    b1 = b1 + 4
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b2 = b2 + 4
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    time.sleep(1)
            elif c1 == 6:
                score = score + 6
                if cr == p1:
                    b1 = b1 + 6
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    time.sleep(1)
                else:
                    b2 = b2 + 6
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    time.sleep(1)
            elif c1 == 0:

                if cr == p1:
                    print("Out {}".format(p1))
                    time.sleep(1)
                    n1 = n1 + 2
                    mc.append(p1)
                    mc.append(b1)
                    b1 = 0
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    wickets = wickets + 1
                    if True:

                        bdic[d1] = mm
                        mm = mm + 1
                else:
                    print("Out {}".format(p2))
                    n2 = n2 + 2
                    time.sleep(1)
                    mc.append(p2)
                    mc.append(b2)
                    b2 = 0
                    print("{} runs {} {}".format(c1, random.choice(psllist.place), random.choice(psllist.quality[0:2])))
                    wickets = wickets + 1
                    if True:

                        bdic[d1] = mm
                        mm = mm + 1


        else:
            print("\nDot ball")
            time.sleep(1)

    print("{} : {} runs\n{} : {}".format(p1,b1,p2,b2))
    time.sleep(1)
    print("\nOver is completed \nScore \nInd vs Pak {}/{} in {} Overs".format(score,wickets,i+1))

    time.sleep(4)
    d1 = random.choice(psllist.pakistan[7:])

print("bowler")
for i,j in bdic.items():
    print("{} = {} Wickets".format(i,j))

for mj in mc:
    print(mj)
