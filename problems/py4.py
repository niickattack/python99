#1.04 (*) Find the number of elements of a list.

#Code
def problem(self):
    d = isinstance(self, list)
    try:    
        assert d == True
    except:
        return 'The input you provided is not a list.'
    else:
        return len(self)

