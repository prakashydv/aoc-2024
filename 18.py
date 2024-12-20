f = open("input.18.txt", "r")
[W, H] = [71,71]
bombs = []
for pair in f:
    pair = pair.split(",")
    pair = [int(i) for i in pair]
    bombs.append(pair)
f.close()

print(f"read {len(bombs)} bomb positions")

import utils as u

grid = u.getEmptyGrid(W, H, 0)
timetoexplode = -1
for [x,y] in bombs:
    grid[y][x] = timetoexplode
    timetoexplode -= 1
grid[0][0] = -1
# BFS

q = []
q.append([0,0,0]) #[x,y,dist]
while len(q) != 0:
    nbr = []
    while len(q) != 0:
        [x,y,dist] = q.pop(0)
        for d in range(4):
            ii = x + u.step_i[d]
            jj = y + u.step_j[d]
            if ii >= 0 and jj >= 0 and ii < W and jj < H:
                if (grid[ii][jj] < 0 and dist < -grid[ii][jj]):
                    grid[ii][jj] = -dist
                    nbr.append([ii,jj,dist+1])
                elif (grid[ii][jj] == 0 or grid[ii][jj] > dist+1):
                    grid[ii][jj] = dist + 1
                    nbr.append([ii,jj,dist+1])
    for n in nbr:
        q.append(n)

u.showGrid(grid)
print(f"ans: {grid[H-1][W-1]}")





