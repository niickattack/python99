#1.02 Find the last but one element in a list.

#Code

def problem(object):
	var1 = len(object)
	var2 = var1 - 2
	try:
		var3 = a[var2]
	except:
		print 'There is a problem with the list provided, it may be empty.'
	else:
		print var3