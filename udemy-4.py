def count_primes(num):
    # check for 0 or 1 input
    if num < 2:
        return 0
    # 2 or greater
    #store our prime numbers
    primes = [2]
    #Counter going up to the input num
    x = 3

    # x is going throught every numbver up to input num
    while x <= num:
        #check if x is prime
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
print(count_primes(100))
