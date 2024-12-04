import queue

f = open("input.5.test.txt")
LAWS = {}
maxref = -1

for rule in f:
	[a,b] = [int(i) for i in rule.split("|")]
	if a in LAWS.keys():
		maxref = maxref if maxref >= len(LAWS[a]) else len(LAWS[a])
		LAWS[a].append(b)
	else:
		LAWS[a] = [b]
f.close()

print(f"nodes:{len(LAWS)} maxref:{maxref}")

f = open("input.5.test.q.txt")

def dfs(n, nodes, visited):
	sorted_nodes = []
	visited = []
	for i in LAWS[n]:
		if (i not in visited):
			[sorted_nodes, visited] = dfs(i, nodes, visited)
			visited.apped(i)
			if (i in nodes):
				sorted_nodes.append(i)
	return [sorted_nodes, visited]

def is_sorted(nodes):
	q = []
	for n in nodes:
		if n in q:
			return False
		dependents = LAWS[n] if n in LAWS.keys() else []
		for dep in dependents:
			if dep in q:
				return False
		q.append(n)
	return True

def get_middle(nodes):
	n = len(nodes)
	return nodes[n//2 + (1 if n%2==0 else 0)]

def get_sorted(nodes):
	####
	return nodes
middles = []
for question in f:
	nodes = [int(i) for i in question.split(",")]
	if is_sorted(nodes):
		print("sorted!", nodes)
		middles.append(get_middle(nodes))
	else:
		middles.append(get_middle(get_sorted(nodes)))

print(middles, sum(middles))



f.close()

