#project: find secret message like meeting time , meeting date, meeting place from a text file

try:
    li=list()
    dic=dict()
    line=0
    x=input('Enter a file name: ')          #enter 'serect' as file name
    f=open(x+'.txt')
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
except FileNotFoundError:
    print('File does not exist!')
