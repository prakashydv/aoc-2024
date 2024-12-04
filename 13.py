import re

f = open("input.13.test.txt")

def getValue(s):
    dX = re.findall(f"X.(\d+)", s)
    dY = re.findall(f"Y.(\d+)", s)
    # print(f"{dX} {dY}")
    return [int(dX[0]), int(dY[0])]

data = []
temp = []
for line in f:
    if line.find("Button A") >= 0:
        delta = getValue(line)
        temp.append(delta)
    elif line.find("Button B") >= 0:
        delta = getValue(line)
        temp.append(delta)
    elif line.find("Prize") >= 0:
        prize = getValue(line)
        temp.append(prize)
        data.append(temp[:])
        temp.clear()

def solve(d):
    [dXa,dYa] = d[0]
    [dXb,dYb] = d[1]
    [pX, pY] = d[2]

    #brute
    for a in range (101):
        b = ((pX+pY) - a * (dXa + dYa))/(dXb + dYb)
        if (b*10)%10 == 0:
            print(f"a:{a} b:{b}")
            return (a*3 + b*1)

ans = 0
for d in data:
    ans += solve(d)

print(ans)