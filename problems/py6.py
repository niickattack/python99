#1.06 (*) Find out whether a list is a palindrome.
#A palindrome can be read forward or backward; e.g. [x,a,m,a,x].

#Code

def problem(a):
    d = isinstance(a, list)
    try:    
        assert d == True
    except:
        return 'The input you provided is not a list.'
    else:
        b = a[::-1]
        if b == a:
            return 'This list is a palindrome.'
        else:
            return 'This list is not a palindrome.'
        
c = 'run'

print problem(c)
