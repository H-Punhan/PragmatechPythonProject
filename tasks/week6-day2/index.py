#1
def square():
    numbers=[]
    truecount=0

    for i in range(0,4):
        data=int(input('write number '))
        numbers.append(data)
    for  i in numbers:
        if numbers[0]==i:
            truecount+=1
    if truecount==4:
        print(numbers[0]*numbers[1])
    else:
        print(sum(numbers))

#2 
def writebig():
    numbers=[]
    truecount=0
    for i in range(0,4):
        data=int(input('write number '))
        numbers.append(data)
    for i in numbers:
        for x in numbers:
            if i>x:
                truecount+=1
        if truecount==3:
            print(i)
        truecount=0

#3
fruits=[
        {
            'fruit':'apple',
            'price':2
        },
        {
            'fruit':'orange',
            'price':3
        },
        {
            'fruit':'pineapple',
            'price':10
        }
    ]

def selectfruit(fruit):
    result=False
    for i in fruits:
        if i["fruit"]==fruit:
            result=True
            return i['price']
    if result==False:
        return 'not founding fruit'

def showfruits():
    for i in range(0,len(fruits)):
        print(f'{i}-{fruits[i]["fruit"]}')
    select=input('select fruit-')
    print(selectfruit(select))


#4
def loginform():
    name=input('name ')
    surname=input('surname ')
    email=input('email')
    password=input('password ')
    passwordagain=input('password again')

    if len(name)<3 or len(name)>11:
        print('ad 11 den boyuk , 3 den kicik  ola bilmez')
    else:
        if len(surname)<5 or len(surname)>15:
            print('soyad 15 den boyuk , 5 den kicik  ola bilmez')
        else:
            if len(email)<10 or len(email)>22:
                print('email 22 herfden boyuk 10 herfden kicik olamasin')
            else:
                email=email.split('@')
                if len(email)==2:
                    if email[0+1]=='gmail.com':
                        print(email)
                else:
                    print('email sefdi')


#5
def sumlist():
    lis=[1,2,3]
    result=0
    for i in lis:
        result+=i
    print(result)


#6
def sortlistbig():
    lis=[1,100,-1,8,90]
    lis.sort()
    lis.reverse()
    print(lis[0])

#7
def sortlistsmall():
    lis=[1,100,-1,8,90]
    lis.sort()
    
    print(lis[0])







