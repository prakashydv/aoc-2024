f = open("input.11.txt", "r")
s = [int(i) for i in f.read().split()]
f.close()

def solve(x):
	result = []
	for s in x:
		if s == 0:
			result.append(1)
		elif len(str(s))%2==0:
			t = str(s)
			n = len(t)
			# print(t,n)
			if n==2:
				result.append(int(t[0]))
				result.append(int(t[1]))
			else:
				result.append(int(t[:n//2]))
				result.append(int(t[n//2:]))
		else:
			result.append(s*2024)
	return result

for i in range(75):
	s = solve(s)
	print(f"[{i+1}] => {len(s)}")

print(len(s))