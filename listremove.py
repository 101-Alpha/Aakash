l = [1,2,3,4,5,6,7,8,9]
for i in range(len(l)+1):
    if i%2!=0:
        l.remove(i)
print(l)
