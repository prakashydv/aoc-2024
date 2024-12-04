f = open("input.19.test.txt", "r")

flags = f.readline()
flags = [flg.strip() for flg in flags.split(", ")]

reqs = []
_ = f.readline()

for req in f:
    reqs.append(req.strip())
f.close()

print(flags, reqs)

def findValidReqs(reqs, flags):
    ans = 0

    return ans

print(findValidReqs(reqs, flags))

