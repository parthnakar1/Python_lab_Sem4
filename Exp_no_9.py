def prime_generator(n):
    p = [True for i in range(n+1)]
    i = 2
    while(i*i<=n):
        if(p[i] == True):
            for j in range(i*i,n+1,i):
                p[j] = False
        i += 1
    return p


test = int(input("Enter number of test cases="))
while(test != 0):
    m = int(input("Lower bound : "))
    n = int(input("Upper bound : "))
    prime = prime_generator(n)
    for i in range(m,n+1):
        if(prime[i]):
            print(i, end=" ")
    test -=1
    print()
    print()