dic= {'roll':[1,2,3,4,], 'name':['akash','ursula','isha','adi'], 'gender':['male','female','female','male']}
for i in range(len(dic['roll'])):
    if dic['gender'][i]=='male':
        print(dic['name'][i])

