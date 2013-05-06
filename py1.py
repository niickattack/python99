# 1.01 (*) Find the last element of a list.
# Example:
# ?- my_last(X,[a,b,c,d]).
# X = d

# Code
def problem(a):
	var1 = len(a)
	var2 = var1 - 1
	try:
		var3 = a[var2]
	except:
		print 'There is a problem with the list provided, it may be empty.'
	else:
		return var3



# Tests
#1
#test1 = [0,1,2,3]
#problem1(test1)

#2
#test2 = []
#problem1(test2)

#3
#test3 = [a,1,3,r,-1]
#problem1(test3)

# Researched Answer
#def problem1(list):
#	return list[-1]

#list = [1,2]
#
#print getlast(list)