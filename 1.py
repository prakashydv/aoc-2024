import time
start = time.process_time()

f = open("input.1.txt")
ans = 0
a, b = [], []
for line in f:
    nums = [int(n) for n in line.split()]
    a.append(nums[0])
    b.append(nums[1])

# a.sort()
# b.sort()
# ans1 = sum([abs(a[i]-b[i]) for i in range(len(a))])

x = {}
for i in b:
    if i in a:
        if i in x.keys():
            x[i] += 1
        else:
            x[i] = 1
ans = 0
for k in x.keys():
    ans += (k * x[k])

f.close()
print(ans)


print(f"---------\ncomputed in: {time.process_time() - start} seconds")