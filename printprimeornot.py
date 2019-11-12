fNo=int(input('Enter the Last Number :'))
for prime in range(2,fNo):
    for i in range(2,prime):
        if prime%i==0:
            print(prime, 'is not prime number')
            break
    else:
        print(prime,'is prime number')