# Question 1

import itertools

def coded_message(L):

    res = []

    for r in range(1, len(L)+1):
        res.append([''.join(str(i) for i in j) for j in itertools.permutations(L, r)])

    res = sorted(list(int(i) for i in itertools.chain.from_iterable(res)), reverse=True)

    for i in res:
        if i % 3 == 0:
            return i
    
    return 0

# Question 2