f = open("input.19.txt", "r")

flags = f.readline()
flags = [flg.strip() for flg in flags.split(", ")]

reqs = []
_ = f.readline()

for req in f:
    reqs.append(req.strip())

maxflaglen = 0
for fl in flags:
    maxflaglen = max(maxflaglen, len(fl))

f.close()
cache = {}
def isValidReq(req):
    if(req in cache.keys()):
        return cache[req]
    if len(req) == 0:
        return True
    if len(req) == 1:
        return req in flags
    if len(req) == 2:
        return ((req[0] in flags) and (req[1] in flags)) or (req in flags)
    for i in range(0, maxflaglen+1):
        prefix = req[:i+1]
        if prefix in flags:
            if isValidReq(req[i+1:]):
                cache[req[i+1:]] = True
                return True
            else:
                cache[req[i+1:]] = False
    return False

def findValidReqs(reqs):
    ans = 0
    for req in reqs:
        ans = (ans + 1) if isValidReq(req) else ans
    return ans

print(f"flags:{len(flags)}, queries:{len(reqs)}, maxlenflag:{maxflaglen}")
print(f"answer 1: {findValidReqs(reqs)}")

