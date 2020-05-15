"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import csv
with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print("First record of texts, {} texts {} at the time {}".format(texts[0][0], texts[0][1], texts[0][2]))
print("Last record of calls, {} calls {}, at the time {} lasting {} seconds"\
.format(calls[-1][0], calls[-1][1],calls[-1][2], calls[-1][3]))


