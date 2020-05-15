"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

import csv
with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

unique_numbers = set()

for row in texts:
	unique_numbers.add(row[0])
	unique_numbers.add(row[1])

for row in calls:
	unique_numbers.add(row[0])
	unique_numbers.add(row[1])

num_of_unique_numbers = len(unique_numbers)

print(f"There are {num_of_unique_numbers} different telephone numbers in the records.")

