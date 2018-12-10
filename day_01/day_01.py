
file =  open('puzzle_input.txt', 'r').read().split('\n')
nrs = list(map(int, file))

# Part 1
freq = 0
for nr in nrs:
	# strip newline character and parse to int
	freq += nr
print('Day 01 part one:',freq)

# Part 2
freq = 0
history = dict()
found = 0
while(not found):
	for nr in nrs:
		if freq not in history:
			history[freq] = True
		else:
			found = 1
			break
		freq += nr

print("Day 01 part two:",freq)