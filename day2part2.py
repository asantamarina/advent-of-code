with open('inputd2p2.txt') as day2input:
    game = day2input.read().strip('\n').split('\n')
    
# print(play)
selectionValues = {'A':1, 'B':2, 'C':3}
wincombination = {'A':'B', 'B':'C', 'C':'A'}
drawcombination = {'A':'A', 'B':'B', 'C':'C'}
losecombination = {'A':'C', 'B':'A', 'C':'B'}

outcomes = {'X': losecombination, 'Y': drawcombination, 'Z': wincombination}
translate = {'X':'A', 'Y':'B', 'Z':'C'}
totalscore = 0

for gameround in game:
    oponentplay = gameround.split(' ')[0]
    playoutcome = gameround.split(' ')[1]
    myplay = outcomes[playoutcome][oponentplay]
    # winplay = wincombination[oponentplay]
    if playoutcome == 'Z':
        totalscore +=6
    elif playoutcome == 'Y':
        totalscore += 3
    totalscore += selectionValues[myplay]
    
print(totalscore)