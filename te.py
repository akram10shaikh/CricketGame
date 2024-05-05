import pickle

import pandas as pd
#
# lst = ["Akram",34,"Adil",43,"Asad",54]
# #
# # with open("doc1.data","wb") as fp:
# #     pickle.dump(lst,fp)
# #     print("File is save")
#
# with open("doc1.data","rb") as dp:
#     s = pickle.load(dp)
#     print(s)
#
# for i in s:
#     print(i)




# with open("doc.txt",'r') as df:

a = []
b = 1
for i in range(2):
    for c in range(2):
        print(c)
    b = b + 1
    a.append(b)
print()
print(a)