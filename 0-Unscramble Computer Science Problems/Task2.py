"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import csv
with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

longest_time_spent = {}

for row in calls:
	if row[0] not in longest_time_spent:
		longest_time_spent[row[0]] = int(row[3])
	else:
		longest_time_spent[row[0]] += int(row[3])

	if row[1] not in longest_time_spent:
		longest_time_spent[row[1]] = int(row[3])
	else:
		longest_time_spent[row[1]] += int(row[3])

max_duration = 0
for phone, duration in longest_time_spent.items():
	if duration > max_duration:
		max_duration = duration
		phone_no = phone

print("{} spent the longest time, {} seconds, on the phone during september 2016.".format(phone_no, max_duration))


