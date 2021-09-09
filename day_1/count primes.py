def countPrimes(n,method=None):
    if method =='sieve':
        '''Sieve Algorithm'''
        primes =[True if x >=2 else False for x in range(0,n)]
        for i in range(2,n):
            if primes[i]:
                for num in range(i*i,n,i):
                    primes[num] =False

        return primes.count(True)
        
    else:
        """ My Solution """
        primes =0
        for num in range(2,n):
            count=0
            for divider in range(1,num +1):
                if num % divider == 0:
                    count += 1
                if count >2:
                    break
            if count <=2:
                primes +=1

        return primes

    