import utils as u

f = open("input.10.txt", "r")
mp = []

for r in f:
	r = r.rstrip()
	mp.append([int(r[i]) for i in range(len(r))])

f.close()

width = len(mp[0])
height = len(mp)

trailheads = []
for i in range(height):
	for j in range(width):
		if mp[i][j] == 0:
			trailheads.append([i,j])

ans = 0
visitedend = u.zilchedGrid(mp, False)

unique = 0
def find(t, p, visitedend):
	global unique
	if p==9:
		visitedend[t[0]][t[1]] = True
		unique += 1
		return visitedend
	else:
		for d in range(4):
			ii = t[0] + u.step_i[d]
			jj = t[1] + u.step_j[d]
			if(u.isGood(mp, ii, jj) and mp[ii][jj] == p+1):
				visitedend = find([ii,jj],p+1, visitedend)
		return visitedend

for t in trailheads:
	v = find(t, 0, u.zilchedGrid(mp, False))
	ans += u.countInGrid(v, True)
	

# for k in mp:
# 	print(k)

print(ans)
print(unique)
