import re


def f(filename):
	valid = 0
	pattern = r'(.)\1'

	with open(filename, 'r') as f:
		for riga in f:
			coppie = re.findall(pattern, riga)
	
			new_dict = {}
			for doppia in coppie:
				new_dict[doppia] = new_dict.get(doppia, 0) + 1
			if any(count == 3 for count in new_dict.values()):
				valid += 1
	return (valid)



file = 'test.txt'
print(f(file))