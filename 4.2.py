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
# print(x)

def X(i, j):
	NWSE = ((x[i-1][j-1] == 'M') and (x[i+1][j+1] == 'S')) or ((x[i-1][j-1] == 'S') and (x[i+1][j+1] == 'M'))
	SWNE = ((x[i+1][j-1] == 'M') and (x[i-1][j+1] == 'S')) or ((x[i+1][j-1] == 'S') and (x[i-1][j+1] == 'M'))
	# if NWSE and SWNE:
	# 	print(f"X-MAS at({i},{j})")
	return NWSE and SWNE

for i in range(1,n-1):
	for j in range(1,m-1):
		if(x[i][j]=='A'):
			ans += 1 if X(i,j) else 0

print(ans)




