# L1 = [1,2,3,4]
# L2 = [a,b,c,d]
# get result [1a,2b,3c,4d]

L1 = [1,2,3,4]
L2 = ['a','b','c','d']
L3= []
for i in range(4):
    L3.append((str(L1)+str(L2)))
print('L3=',L3)