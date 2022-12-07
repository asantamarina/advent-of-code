#Day4
#Abel Santamarina
#AdventOfCode2022

with open('inputd4.txt') as day4input:
    totalsections = day4input.read().strip('\n').split('\n')
    
WrongAssignments = []

for section in totalsections:
    section1 = section.split(',')[0]
    section2 = section.split(',')[1] 
    lowend1 = int(section1.split('-')[0])
    highend1 = int(section1.split('-')[1])
    lowend2 = int(section2.split('-')[0])
    highend2 = int(section2.split('-')[1])
    
    Elf1 = set(range(lowend1,highend1 + 1))
    Elf2 = set(range(lowend2,highend2 + 1))
    
    if len(Elf1) > len(Elf2):
        WrongAssignments.append(Elf1.issuperset(Elf2))
    else:
        WrongAssignments.append(Elf2.issuperset(Elf1))
    
print(WrongAssignments.count(True))
    
    