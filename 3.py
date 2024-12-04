import re

f = open("input.3.txt")

# ans = 0
# for txt in f:
# 	x = re.findall("mul\((\d+),(\d+)\)", txt)
# 	for p in x:
# 		ans += int(p[0])*int(p[1])
# print(ans)

ans = 0
text = ""
for t in f:
	text += t

does = text.split("do()")
for dos in does:
	actuallydo = dos.split("don't()")[0]
	x = re.findall("mul\((\d+),(\d+)\)", actuallydo)
	for p in x:
		ans += int(p[0])*int(p[1])

print(ans)

