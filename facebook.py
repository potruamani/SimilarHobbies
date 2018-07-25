# -*- coding: utf-8 -*-

import re
from collections import Counter
from itertools import chain
lines = []
hobbies = []
pop=[]
circlesFile = open('circles.txt','w')
popularFile = open('popular.txt','w')
with open("hobbies.txt") as f:
     for l in f:
         number_strings = re.split(r',\s*(?=[^)]*(?:\(|$))', l) 
         number = [n for n in number_strings] 
         lines.append(number)
for i in range(len(lines)):
  hobbies.extend(set(lines[i]))
s_hobbies = set(hobbies)
ls_alpha = [i for i in s_hobbies if not i.isdigit()]
ls_alpha.remove('')
common = []
for x in range(len(ls_alpha)):
    s = ls_alpha[x]
    temp=[]
    for y in range(len(lines)):
        if s in lines[y]:
            temp.append(lines[y][0])
        else:
            continue
    common.append(temp)

x = int(input("Enter no.of common hobbies"))

if x == 1:
    for i in range(len(common)):
        pop.append(common[i][0])
        circlesFile.write(', '.join(common[i]))
        circlesFile.write("\t")
        circlesFile.write(ls_alpha[i])
        circlesFile.write("\n")
else:
    c_h=[]
    for i in range(len(common)):
         for j in range(i+1, len(common)):
            temp1 = (list(set(common[i]).intersection(common[j])))
            if x > 2:
                for k in range(j+1, len(common)):
                    temp2 =(list(set(temp1).intersection(common[k])))
                    c_h.append(ls_alpha[i])
                    c_h.append(ls_alpha[j])
                    c_h.append(ls_alpha[k])                     
                    if not temp2 or len(temp2) <= 1:
                        c_h.clear()
                        continue
                    else:
                        pop.append(temp2)
                        circlesFile.write(', '.join(temp2))
                        circlesFile.write("\t")
                        circlesFile.write(', '.join(c_h))
                        circlesFile.write("\n")
                        c_h.clear()
            else:
                if not temp1 or len(temp1) <= 1:
                    c_h.clear()
                    continue
                else:
                    c_h.append(ls_alpha[i])
                    c_h.append(ls_alpha[j])
                    pop.append(temp1)
                    circlesFile.write(', '.join(temp1))
                    circlesFile.write("\t")
                    circlesFile.write(', '.join(c_h))
                    circlesFile.write("\n")
                    c_h.clear()
counts = Counter(chain.from_iterable(pop))
popularFile.write(str(', '.join([str(i) for i in counts.most_common()])))
print(str(', '.join([str(i) for i in counts.most_common()])))
ls_alpha.clear()
pop.clear()
common.clear()
lines.clear()