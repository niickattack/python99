#1.02 Find the last but one element in a list.

#Code

def problem(self):
	d = isinstance(self, list)
	try:	
		assert d == True
	except:
		return 'The input you provided is not a list.'
	else:
		a = len(self)
		e = 0
		b = a - 2
		if b >= e:
			c = self[b]
		elif b == -1:
			c = 'The list you provided contains only one element.'
		else:
			c = 'The list you provided is empty.'	
		return c