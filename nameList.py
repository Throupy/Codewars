#Structure of input: [{'name':'owen'},{'name':'corey'}]
#>> owen and corey
def namelist(names):
	eNames = [name['name'] for name in names]
	if len(names) < 3:
		return ' & '.join([x for x in eNames])
	else:
		x = ''
		lastName = eNames[-1]
		eNames.remove(lastName)
		return ', '.join([x for x in eNames]) + f" & {lastName}"

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
    