L1=[1,"red",2,3]
L2=["apple","orange","mango"]
L3=["php","python","java"]

#concatenate L1 and L2
#add L1 in L2
#L3, add a programming language
#remove unwanted data from L1
L4=L1+L2

#L4.append(str(L1)+str(L2))
print(L4)
L1.extend(L2)
print(L1)
L3.append("JS")
print(L3)
L1.remove("red")
print(L1)
print(L1.pop)
l5=[]
for fruits in L2:
    l5.append(fruits)
    print(fruits)

print(l5)