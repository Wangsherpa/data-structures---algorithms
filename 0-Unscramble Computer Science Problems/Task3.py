"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


bang_code = '(080)'

# Function to get all the codes of numbers called by banglore numbers
def get_list_of_codes(calls):

	no_called_from_bang = set()

	for row in calls:

		if bang_code in row[0]:
			if '(' in row[1]:
				no_called_from_bang.add(row[1].split(')')[0][1:])
			elif '140' in row[0][:3]:
				no_called_from_bang.add('140')
			else:
				no_called_from_bang.add(row[1][:4])

	return no_called_from_bang

codes = sorted(get_list_of_codes(calls))

print("The numbers called by people in Bangalore have codes:")
for code in codes:
	print(code)

# This function will return the percentage of the calls made from banglore to banglore
def percentage(calls):
	count = 0
	for row in calls:
		if bang_code in row[0] and bang_code in row[1]:
			count += 1

	return count / len(calls) * 100


print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(percentage(calls)))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
