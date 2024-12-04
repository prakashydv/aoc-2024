import re

f = open("input.7.txt")

ans = 0

eqn = []
for e in f:
	e = e.split(':')
	eqn.append([int(e[0])]+[int(i) for i in e[1].split()])
f.close()


def solves(lhs,rhs):
	if len(rhs) == 1:
		return lhs == rhs[0]
	else:
		if (rhs[0] > lhs):
			return False
		m = rhs[0] * rhs [1]
		a = rhs[0] + rhs [1]
		return solves(lhs,[m] + rhs[2:]) or solves(lhs, [a] + rhs[2:])

def solves2()

# print(eqn)
for e in eqn:
	if solves2(e[0], e[1:]):
		ans += e[0]

# print(ans)

