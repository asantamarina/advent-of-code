#Day3
#Abel Santamarina
#AdventOfCode2022

import string

prioritylist = string.ascii_lowercase + string.ascii_uppercase

with open('inputd3.txt') as day3input:
    runsacks = day3input.read().strip('\n').split('\n')
    
prioritytotal = []
runsackgroups = [runsacks[i:i + 3] for i in range(0, len(runsacks), 3)]

for runsackgroup in runsackgroups:
    commonitem = ''.join(set(runsackgroup[0]).intersection(runsackgroup[1]).intersection(runsackgroup[2]))
    prioritytotal.append(prioritylist.index(commonitem) + 1)

print(sum(prioritytotal))