maths = {'Roll no.' : [1,2,3,4,5], 'Name' : ['Aakash', 'Sameer', 'Ursula', 'Isha', 'Laxmi']}
print(maths["Roll no."][0],maths['Name'][0]) #direct print
R=maths['Roll no.'] #creating variable for key values
N=maths['Name']
print(R[0],N[0])
data = int(input('Roll No. :'))
temp=0
for i in range(len(R)):
    if R[i]==data:
        temp=i
print(N[temp])