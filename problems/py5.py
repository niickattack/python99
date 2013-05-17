#1.05 (*) Reverse a list.

#Code
def problem(self):
    d = isinstance(self, list)
    try:    
        assert d == True
    except:
        return 'The input you provided is not a list.'
    else:
        return self[::-1]