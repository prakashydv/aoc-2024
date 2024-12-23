f = open("input.23.txt")

graph = {}
for p in f:
    [a,b] = p.strip().split("-")
    if(a in graph.keys()):
        graph[a].append(b)
    else:
        graph[a] = [b]
    if(b in graph.keys()):
        graph[b].append(a)
    else:
        graph[b] = [a]
f.close()

triplets = []



v = [] #visited

def gettriplet(n2,n1):
    ret = []
    for n3 in graph[n2]:
        if n1 in graph[n3]:
            ret.append('-'.join(sorted([n1,n2,n3])))
    return ret

for n in graph.keys():
    if n in v:
        continue
    v.append(n)
    for nbr in graph[n]:
        t = gettriplet(nbr,n)
        if len(t) > 0:
            triplets.extend(t)

ans = 0
triplets = list(set(triplets))
for triplet in triplets:
    if triplet.find('t') >= 0:
        ans += 1
        print(triplet)

print(ans)