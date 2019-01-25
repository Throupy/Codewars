#Inputs list and you must find the number that appears an odd amount of times
def find_it(seq):
	for x in seq:
		if not seq.count(x) % 2 == 0:
			return x
