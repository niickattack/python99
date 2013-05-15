#1.03 (*) Find the K'th element of a list.
#The first element in the list is number 1.
#Example:
#?- element_at(X,[a,b,c,d,e],3).
#X = c

#Code
def problem(K, List):
    d = isinstance(List, list)
    n = isinstance(K, int)
    try:    
        assert d == True
    except:
        return 'The input you provided is not a list.'
    else:
        try:
            assert n == True
        except:
            return 'You did not provide an int.'
        else:
            if K <= len(List) - 1:
                return List[K]
            else:
                return 'The list you provided contains less than ' + str(K) + ' elements.'