"""a = 1
b = 109900
c = 126900

f = 1
d = 2
e = 2

while not g:

    g = int(d)
    g *= e
    g -= b

    if not g:

        f = 0
    
    e += 1

    g = int(e)
    g -= b

    if not g:"""

def prime_checker(num):

    if num > 1:
    # Iterate from 2 to n / 2
        for i in range(2, int(num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return 0
                break
        else:
            return 1
    else:
        return 0

b = 99
b *= 100
b += 100000
c = int(b)
c += 17000

tot = 0

for i in range(b, c+1, 17):

    tot += 1 if not prime_checker(i) else 0

print(tot)
