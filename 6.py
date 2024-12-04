import re
import utils as u

u.printRecursionLimit()
u.setRecursionLimit(10000)

f = open("input.6.txt")

m = []
for txt in f:
	txt = txt.rstrip()
	m.append([c for c in txt])

f.close()

height = len(m)
width = len(m[0])

print("size: ", height, width)

def getinitpos():
	for i in range(height):
		for j in range(width):
			if (m[i][j] == '^'):
				return [i,j]
	print("no onit position found")
	return [-1,-1]

v = [[[False for _ in range(width)] for _ in range(height)] for _ in range(4)]

direction = 0
step_i = [-1, 0, 1, 0]
step_j = [0, 1, 0, -1]

def canstep(i, j, d):
	if i >= 0 and j >= 0 and i < height and j < width and m[i][j] in ['.','^']:
		if v[d][i][j] == False:
			return True
	return False

def move(i,j, d, ans):
	beenhere = False
	for k in range(4):
		beenhere = beenhere or v[(d+k)%4][i][j]
	v[d][i][j] = True
	ans = ans if beenhere else (ans + 1)
	# print(f"move {d}: {i},{j} --> {ans}")

	#moves
	for delta in range(4):
		dd = (d+delta)%4
		[ii,jj] = u.getNextStep(i,j,dd)
		if (u.isBoundary(ii, jj, height, width)):
			return ans
		if (canstep(ii,jj,dd)):
			return move(ii,jj,dd, ans)
	return ans

[i,j] = getinitpos()
print("answer: ", move(i, j, 0, 0))



