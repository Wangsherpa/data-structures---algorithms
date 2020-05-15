"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import csv

with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# This function set of telemarketers numbers

def get_telemarketers(calls):
	tele_list = set()

	for row in calls:
		if '140' in row[0][:3]:
			tele_list.add(row[0])
	return tele_list


def possible_telemarketers(calls, texts):
	possible_teles = set()

	for row in calls:
		possible_teles.add(row[0])
	for row in calls:
		if row[1] in possible_teles:
			possible_teles.remove(row[1])
	for row in texts:
		if row[0] in possible_teles:
			possible_teles.remove(row[0])
		if row[1] in possible_teles:
			possible_teles.remove(row[1])
	return possible_teles


possible_teles = possible_telemarketers(calls, texts)
confirm_teles = get_telemarketers(calls)
tele_list_sorted = sorted(possible_teles.union(confirm_teles))

print("These numbers could be telemarketers: ")
for no in tele_list_sorted:
	print(no)


