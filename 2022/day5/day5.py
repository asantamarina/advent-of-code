#Day5
#Abel Santamarina
#AdventOfCode2022

def transposeTable(l1, l2):
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

def parseFile(cargostacks):
    # Parse Stacks
    stacks = cargostacks.split('\n'*2)[0]
    stacks = stacks.split('\n')[0:-1]
    table = []
    for row in stacks:
        table.append([row[i:i + 4].strip(' []') for i in range(0, len(row), 4)])
    transposedtable = transposeTable(table, [])
    cleantable = [[s for s in row if s] for row in transposedtable]
    
    #Parse Instructions
    instructions = cargostacks.split('\n'*2)[1].split('\n')
      
    return cleantable, instructions
        

with open('inputd5.txt') as day5input:
    cargostacks = day5input.read().strip('\n')

#Parse File
stacks, instructions = parseFile(cargostacks)

for instruction in instructions:
    moves = [int(s) for s in instruction.split() if s.isdigit()]
    nomoves = moves[0]
    movefromidx = moves[1] - 1
    movetoidx = moves[2] - 1
    for i in range(nomoves):
        stacks[movetoidx].insert(0, stacks[movefromidx][0])
        stacks[movefromidx].pop(0)
    
topstack = ''.join([stack[0] for stack in stacks])
print(topstack)