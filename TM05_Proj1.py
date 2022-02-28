#project: find meeting time , meeting date

li=list()
dic=dict()
line=0
f=open('secret.txt')
li=f.read().replace('\n',' \n ').split(' ')
for i in li:
    dic[i]=li.count(i)

for j in dic:
    max=dic[j]
    word=j
    for k in dic:
        if max<dic[k]:
            max=dic[k]
            word=k

if int(dic['\n'])>12:
    time=int(dic['\n'])%12
    t='PM'
else:
    time=(dic['\n'])
    t='AM'
    
print('Meeting time:',time,t)
print('Meeting place:',word.capitalize(),'Street')
