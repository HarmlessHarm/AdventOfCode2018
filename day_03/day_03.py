import re
import numpy as np

file = open('puzzle_input.txt', 'r').read().split('\n')

claims = list()
for el in file:
	claims.append(list(map(int, re.match('#([0-9]+)\s@\s([0-9]+),([0-9]+):\s([0-9]+)x([0-9]+)', el).groups())))

sheet = np.zeros([1000,1000])
for i, x, y, w, h  in claims:
	sheet[y:y+h, x:x+w] += 1

print("Day 03 part one:",len(np.where(sheet > 1)[0]))


for i, x, y, w, h  in claims:
	part = sheet[y:y+h, x:x+w]

	if np.all(part == 1):
		single = i
		break

print("Day 03 part two:", single)
