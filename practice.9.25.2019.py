Even=[]
Odd=[]
for i in range(1,101):
    if i%2==0:
        Even.append(i)
    else:
        Odd.append(i)
print('Odd=', Odd)
print('Even = ', Even)
