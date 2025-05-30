'''
Instructions
- Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches.
- Assign each captured group to the corresponding keys in the dictionary.
- Complete the positional method to print out the captured groups. Use the values corresponding to each key in the dictionary.
'''

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}

# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))