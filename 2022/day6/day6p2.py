#Day6
#Abel Santamarina
#AdventOfCode2022

with open('inputd6.txt') as day6input:
    datastream = day6input.read().strip('\n')

markeridx = 14
dsidx = markeridx
rollingmarker = datastream[0:dsidx]
rollingmarkerset = set(rollingmarker)

while len(rollingmarkerset) < markeridx:
    rollingmarker = rollingmarker[1:] + datastream[dsidx]
    rollingmarkerset = set(rollingmarker)
    dsidx += 1
    
print(dsidx)