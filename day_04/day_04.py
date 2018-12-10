from datetime import datetime, timedelta
import re
import pprint


file = open('puzzle_input.txt', 'r').read().split('\n')

parsed = list()
for line in file:
	date, action = (re.match('\[(.*)\]\s(.+)', line).groups())
	date = datetime.strptime(date, '%Y-%m-%d %H:%M')
	parsed.append((date,action))

parsed.sort()

data = dict()
guard = None
new_shift = None
zero_time = datetime.strptime('00:00', '%H:%M')
for date, action in parsed:
	match = re.match('.*#([0-9]+).*', action)
	if match:
		if new_shift:
			data[guard] = [x+y for x,y in zip(new_shift, data[guard])]
		guard = int(match.groups()[0])
		if guard not in data:
			data[guard] = [0]*60
		new_shift = [0]*60
		if date.time().hour > 0:
			td = timedelta(days=1)
			date = date + td
		date = date.replace(hour=0, minute=0)
	elif action == 'falls asleep':
		sleep_start = date.time().minute
	elif action == 'wakes up':
		sleep_end = date.time().minute
		length = sleep_end - sleep_start
		new_shift[sleep_start:sleep_end] = [1]*length

longest_sleep = 0
best_min = None
sleepy_guard = None
for guard, shifts in data.items():
	if sum(shifts) > longest_sleep:
		longest_sleep = sum(shifts)
		best_min = shifts.index(max(shifts))
		sleepy_guard = guard

print('Guard: {}, total mins: {}, best min: {}'.format(sleepy_guard, longest_sleep, best_min))
print("Day 04 part one:", sleepy_guard * best_min)