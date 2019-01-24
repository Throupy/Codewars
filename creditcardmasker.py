# return masked string
def maskify(cc):
	suffix = cc[-4:]
	return len(cc[:-4]) * '#' + suffix

print(maskify("4556364607935616"))
# Should output >> ############5616
