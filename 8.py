import utils as u

[_,_,grid] = u.getStrGrid("input.8.txt")

antigrid = u.zilchedGrid(grid, 0)

locationDict = u.getGridLocations(grid, ['.'])
uniq = 0

for t in locationDict.keys():
    locs = locationDict[t]
    for a in locs:
        [ai,aj] = a
        for b in locs:
            [bi,bj] = b
            if (ai==bi and aj == bj):
                continue
            [di, dj] = [bi-ai, bj-aj]
            n1 = [ai-di, aj-dj]
            n2 = [bi+di, bj+dj]
            if u.isGood(grid, n1[0], n1[1]):
                if (antigrid[n1[0]][n1[1]] == 0):
                    uniq += 1
                antigrid[n1[0]][n1[1]] += 1
            if u.isGood(grid, n2[0], n2[1]):
                if (antigrid[n2[0]][n2[1]] == 0):
                    uniq += 1
                antigrid[n2[0]][n2[1]] += 1

print(f"Unique antinodes: {uniq}")
