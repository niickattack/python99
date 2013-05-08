# 1.01 (*) Find the last element of a list.
# Example:
# ?- my_last(X,[a,b,c,d]).
# X = d

# Code
def problem(self):
	print self
	print type(self)
	print list
	try:
		self.d = self.assertIsInstance(type(self), list)
	except:
		return 'The input you provided is not a list.'
	else:
		self.a = len(self)
		self.b = self.a - 1
		self.c = self[self.b]
		return self.c
	
a = [1,2,3]

print problem(a)
	