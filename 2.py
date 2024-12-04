import time
start = time.process_time()

#####################

def loose_check(report):
    print("---> ",report)
    prev = report[0]
    if report[0] == report[1]:
        return strict_check(report[1:])
    inc = report[1] > report[0]
    i = 1
    while i < len(report):
        diff = report[i] - report[i-1]
        if diff == 0:
            return strict_check(report[:i] + report[i+1:])
        if inc != (diff >= 0):
            return strict_check(report[:i] + report[i+1:])
        if (abs(diff) < 1) or (abs(diff) > 3):
            return strict_check(report[:i] + report[i+1:])
        # print(diff)
        # print(report)
        i+=1
    return 1

def strict_check(report):
    print("   > ",report)
    prev = report[0]
    if report[0] == report[1]:
        return 0
    inc = report[1] > report[0]
    i = 1
    while i < len(report):
        diff = report[i] - report[i-1]
        if diff == 0:
            return 0
        if inc != (diff >= 0):
            return 0
        if (abs(diff) < 1) or (abs(diff) > 3):
            return 0
        # print(diff)
        # print(report)
        i+=1
    return 1


f = open("input.2.txt")
# f = open("input.2.2.test.txt")
ans = 0
for report in f:
    report = [int(i) for i in report.split()]
    a = loose_check(report)
    print("  ", a)
    ans += 1 if a else 0

###############

f.close()
print(ans)


print(f"---------\ncomputed in: {int((time.process_time() - start) * 1000)} ms")

## not 274 500