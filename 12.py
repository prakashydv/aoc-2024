import utils

[height, width, mp] = utils.getStrGrid("input.12.txt")

[rmp, region_count] = utils.colorGrid(mp)

print(f"region count: {region_count}")
# perimeters = [0 for _ in range(region_count)]
# region_population = [0 for _ in range(region_count)]
# for i in range(len(rmp)):
# 	for j in range(len(rmp[0])):
# 		p = 0
# 		if i == 0 or i == height-1:
# 			p = p+1
# 		if j == 0 or j == width-1:
# 			p = p+1
# 		for d in range(4):
# 			ii = i + utils.step_i[d]
# 			jj = j + utils.step_j[d]
# 			if utils.isGood(rmp, ii, jj) and rmp[i][j] != rmp[ii][jj]:
# 				p = p + 1
# 		perimeters[rmp[i][j]] += p
# 		region_population[rmp[i][j]] += 1

[region_sides, region_population] = utils.regionSides(rmp, region_count)

ans = 0
for i in range(region_count):
	# print(f"{i} region {region_population[i]} cells x {perimeters[i]} perimeter = {region_population[i] * perimeters[i]}")
	# ans += (region_population[i] * perimeters[i])
	ans += (region_population[i] * region_sides[i])

# utils.showGrid(rmp)
# print(f"perimeters: {perimeters}")
print(f"ans: {ans}")

