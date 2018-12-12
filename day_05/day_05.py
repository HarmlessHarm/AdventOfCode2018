import string

def reactPoly(polymer):
	count = 0
	removed = True
	iteration = 0
	skip = False
	while(removed):
		removed = False
		iteration += 1
		new_poly = polymer.copy()
		for i in range(len(polymer) - 1):
			if skip:
				skip = False
				continue

			c1 = polymer[i]
			c2 = polymer[i+1]
			if (c1.islower() and c2.isupper() and c1.upper() == c2) or \
				 (c2.islower() and c1.isupper() and c2.upper() == c1):
				count += 2
				removed = True
				new_poly[i] = 0
				new_poly[i+1] = 0
				i += 1
				skip = True

		polymer = list(filter(lambda a: a != 0, new_poly))

	return(polymer)


polymer = open('puzzle_input.txt', 'r').read()
polymer = list(polymer)

print("Day 05 part one:", len(reactPoly(polymer)))

best = float('inf')
for char in list(string.ascii_lowercase):
	print("Checking", char)
	new_poly = list(filter(lambda a: a != char, polymer))
	new_poly = list(filter(lambda a: a != char.upper(), new_poly))
	length = len(reactPoly(new_poly))
	if length < best:
		best = length

print("Day 05 part two:", best)