
lines =  open('puzzle_input.txt', 'r').read().split('\n')

# Part 1
two = 0
three = 0
for el in lines:
	add_two = 0
	add_three = 0
	for c in el:
		if el.count(c) == 2:
			add_two = 1
		if el.count(c) == 3:
			add_three = 1
	two += add_two
	three += add_three

print("Day 02 part one:", two * three)

# Part 2
result = 0
for el in lines:
	for check in lines:
		count = 0
		for i, c in enumerate(el):
			if check[i] != c:
				count += 1
			if count > 1:
				break
		if count == 1:
			result = (check, el)
			break
	if result:
		break

print("Day 02 part two:", *result)
			

