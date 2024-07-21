candidates = set(primes(1,1000000))
copy = candidates.copy()

from itertools import permutations
 
def circles(n):
    digits = len(str(n))
    cycles = []
    next_cycle = str(n)
    n = str(n)
    for i in range(digits):
        cycles = cycles + [int(n)]
        n = str(n)[1:] + str(n)[:1]
    return set(cycles).issubset(candidates)
    
print(len(list(filter(circles, copy))))

print(circles(197))


