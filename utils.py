
import sys

def printRecursionLimit():
	print(f"Recursion Limit: {sys.getrecursionlimit()}")

def setRecursionLimit(v):
	print(f"Set Recursion Limit To: {v}")
	sys.setrecursionlimit(v)

def getNumGrid(filename):
	f = open(filename, "r")
	mp = []
	for r in f:
		r = r.rstrip()
		mp.append([int(r[i]) for i in range(len(r))])
	f.close()
	return [len(mp), len(mp[0]) , mp]

def getStrGrid(filename):
	f = open(filename, "r")
	mp = []
	for r in f:
		r = r.rstrip()
		mp.append([r[i] for i in range(len(r))])
	f.close()
	return [len(mp), len(mp[0]) , mp]

def zilchedGrid(mp, z):
	return [[ z for _ in range(len(mp[0]))] for _ in range(len(mp))]

step_i = [-1, 0, 1, 0]
step_j = [0, 1, 0, -1]

def isGood(mp,i,j):
	return i >= 0 and j >= 0 and i < len(mp) and j < len(mp[0])

def showGrid(mp):
	for r in mp:
		print(''.join(str(r)))


def colorRegion(rmp, mp, i, j, c):
	rmp[i][j] = c
	for d in range(4):
		ii = i + step_i[d]
		jj = j + step_j[d]
		if isGood(mp,ii,jj) and mp[ii][jj] == mp[i][j] and rmp[ii][jj] == -1:
			rmp = colorRegion(rmp, mp, ii, jj, c)
	return rmp

def colorGrid(mp):
	colorCount = 0
	rmp = zilchedGrid(mp, -1)
	for i in range(len(mp)):
		for j in range(len(mp[0])):
			if (rmp[i][j] == -1):
				rmp = colorRegion(rmp, mp, i, j, colorCount)
				colorCount += 1
				# showGrid(rmp)

	return [rmp, colorCount]

def regionSides(mp, region_count):
	region_sides = [0 for _ in range(region_count)]
	region_population = [0 for _ in range(region_count)]

	############# ???

	return [region_sides, region_population]

def readNumSequenceFromFile(filename):
	f = open(filename, "r")
	line = f.read()
	ret = [int(line[i]) for i in range(len(line))]
	f.close()
	return ret

def countInGrid(grid, value):
	ans = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			ans = ans + 1 if grid[i][j] == value else ans
	return ans

def getNextStep(i,j, d):
	return [i + step_i[d], j + step_j[d]]

def isBoundary(i, j, height, width):
	if i<0 or j<0:
		return True
	if i>height-1 or j>width-1:
		return True
	return False

def getGridLocations(grid, ignoreList):
	h = len(grid)
	w = len(grid[0])
	loc = {}
	for i in range(h):
		for j in range(w):
			v = grid[i][j]
			if (v in ignoreList):
				continue
			else:
				if v in loc.keys():
					loc[v].append([i,j])
				else:
					loc[v] = [[i,j]]
	return loc
