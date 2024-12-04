import re
f = open("input.4.txt")

# ans = 0
# for txt in f:
# 	x = re.findall("mul\((\d+),(\d+)\)", txt)
# 	for p in x:
# 		ans += int(p[0])*int(p[1])
# print(ans)

ans = 0
x = []
for line in f:
	line = line.rstrip()
	x.append([line[i] for i in range(len(line))])

n = len(x)
m = len(x[0])

print(n,m)

def N(i,j):
	if (i >= 3):
		return x[i-1][j] == "M" and x[i-2][j] == "A" and x[i-3][j] == "S"
	return 0
def E(i,j):
	if (j >= 3):
		return x[i][j-1] == "M" and x[i][j-2] == "A" and x[i][j-3] == "S"
	return 0
def S(i,j):
	if (i < n-3):
		return x[i+1][j] == "M" and x[i+2][j] == "A" and x[i+3][j] == "S"
	return 0
def W(i,j):
	if (j < m-3):
		return x[i][j+1] == "M" and x[i][j+2] == "A" and x[i][j+3] == "S"
	return 0

def NE(i,j):
	if (i >= 3 and j >= 3):
		return x[i-1][j-1] == "M" and x[i-2][j-2] == "A" and x[i-3][j-3] == "S"
	return 0
def NW(i,j):
	if (j < m-3 and i >= 3):
		return x[i-1][j+1] == "M" and x[i-2][j+2] == "A" and x[i-3][j+3] == "S"
	return 0
def SE(i,j):
	if (i < n-3 and j>=3):
		return x[i+1][j-1] == "M" and x[i+2][j-2] == "A" and x[i+3][j-3] == "S"
	return 0
def SW(i,j):
	if (i < n-3 and j < m-3):
		return x[i+1][j+1] == "M" and x[i+2][j+2] == "A" and x[i+3][j+3] == "S"
	return 0

# print(x)

for i in range(n):
	for j in range(m):
		if(x[i][j]=='X'):
			ans += sum([E(i,j),W(i,j),N(i,j),S(i,j),NW(i,j),NE(i,j),SW(i,j),SE(i,j)])

print(ans)




