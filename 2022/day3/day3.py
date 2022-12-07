#Day3
#Abel Santamarina
#AdventOfCode2022

import string

prioritylist = string.ascii_lowercase + string.ascii_uppercase

with open('inputd3.txt') as day3input:
    runsacks = day3input.read().strip('\n').split('\n')
    
prioritytotal = []

for runsack in runsacks:
    rssize = len(runsack)
    compartment1 = runsack[0:int(rssize/2)]
    compartment2 = runsack[int(rssize/2):]
    
    # commonitem = ''.join([item for item in compartment1 if item in compartment2])
    commonitem = ''.join(set(compartment1).intersection(compartment2))
    prioritytotal.append(prioritylist.index(commonitem) + 1)
    
print(sum(prioritytotal))