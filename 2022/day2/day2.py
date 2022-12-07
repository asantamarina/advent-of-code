#Day2
#Abel Santamarina
#AdventOfCode2022


with open('inputd2.txt') as day2input:
    game = day2input.read().strip('\n').split('\n')
    
# print(play)
selectionValues = {'A':1, 'B':2, 'C':3}
wincombination = {'A':'B', 'B':'C', 'C':'A'}
translate = {'X':'A', 'Y':'B', 'Z':'C'}
totalscore = 0

for gameround in game:
    oponentplay = gameround.split(' ')[0]
    myplay = translate[gameround.split(' ')[1]]
    winplay = wincombination[oponentplay]
    if myplay == winplay:
        totalscore +=6
    elif myplay == oponentplay:
        totalscore += 3
    totalscore += selectionValues[myplay]
    
print(totalscore)
