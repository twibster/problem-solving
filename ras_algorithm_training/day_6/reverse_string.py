def reverseString(s,sol = 'dummy'): 
    '''my dummy solution'''
    if sol == 'dummy':
        counter= 0
        for r in range(len(s)):
            last = s[-1]
            s.insert(counter,last)
            s.pop(-1)
            counter += 1

    '''fast as hell boy'''
    else:
        s.reverese()
        
    return s