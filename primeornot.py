print('find out whether a number is prime or not')
n = int(input('Enter the Number : '))
ans = True
for prime in range(2,n):
    if ans % n == 0:
        ans = False
        break
print(ans)