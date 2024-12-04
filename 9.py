import utils as u


input = u.readNumSequenceFromFile("input.9.txt")
compressed_disk = []

file = 0
isfile = True
for c in input:
    compressed_disk.extend([(str(file) if isfile else '.') for _ in range(c) ])
    file = file + 1 if isfile else file
    isfile = not isfile

# print(''.join(compressed_disk))

i = 0
j = len(compressed_disk)-1

while i<j and j >= 0 and i < len(compressed_disk):
    if compressed_disk[j] == '.':
        j-=1
        continue
    if compressed_disk[i] != '.':
        i+=1
        continue
    compressed_disk[i] = compressed_disk[j]
    compressed_disk[j] = '.'
    i+=1
    j-=1

cheksum = 0
for i in range(len(compressed_disk)):
    if compressed_disk[i] != '.':
        cheksum += int(compressed_disk[i])*int(i)

print(cheksum)