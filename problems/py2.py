#1.02 Find the last but one element in a list.

#Code

def problem(a):
	var1 = len(a)
	var2 = var1 - 2
	try:
		var3 = a[var2]
	except:
		return 'There is a problem with the list provided, it may not be a list, or it may be empty.'
	else:
		return var3