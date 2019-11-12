print('print the prime no. upto 100')


#for i in range(1,100):
 #   if i>2:
  ##         break

    #if i>3:
     #   if i%3==0:
      #      break
    #if i>5:
     #   if i%5==0:
      #      break
    #if i>7:
     #   if i%7==0:
      #      break
   # print(i)

for prime in range(1,100):
    if prime > 1:
        for i in range(2,prime):
            if prime%i == 0:
                print(prime, 'is not a prime number')
                break
        else:
            print(prime, 'is a prime number')
