#Day1
#Abel Santamarina
#AdventOfCode2022

with open('inputd1p2.txt') as day1input:
    totalcalories = day1input.read().strip('\n')
    
# print(totalcalories)

Elves = totalcalories.split('\n'*2)
ElfTotal = []
# print(Elves)
for Elf in Elves:
    totalcals = sum(int(cals) for cals in Elf.split('\n'))
    ElfTotal.append(totalcals)

ElfTotal.sort(reverse=True)
Top3 = sum(ElfTotal[0:3])
print(Top3)
