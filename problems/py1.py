# 1.01 (*) Find the last element of a list.
# Example:
# ?- my_last(X,[a,b,c,d]).
# X = d

# Code
def problem(self):
	d = isinstance(self, list)
	try:	
		assert d == True
	except:
		return 'The input you provided is not a list.'
	else:
		a = len(self)
		e = 0
		b = a - 1
		if b >= e:
			c = self[b]
		else:
			c = 'The list you provided is empty.'
		return c