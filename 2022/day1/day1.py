#Day1
#Abel Santamarina
#AdventOfCode2022

with open('input.txt') as day1input:
    totalcalories = day1input.read().strip('\n')
    
# print(totalcalories)

Elves = totalcalories.split('\n'*2)
ElfTotal = []
# print(Elves)
for Elf in Elves:
    totalcals = sum(int(cals) for cals in Elf.split('\n'))
    ElfTotal.append(totalcals)

MaxCals = max(ElfTotal)
print(MaxCals)
