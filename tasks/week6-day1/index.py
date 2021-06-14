#1

def write1():
    message=input('write message')

    print(message)

#2

def toUpperletter():
        
    name=list(input('name'))
    surname=list(input('surname'))

    name[0]=name[0].upper()
    surname[0]=surname[0].upper()

    newname=''
    newsurname=''
    for i in name:
        newname+=i

    for i in surname:
        newsurname+=i

    result=f'Salam {newname} {newsurname}'
    

    print(result)

#3

def writesep():
    print('Baku','Sumqayit','Samaxi','Gence',sep=' ')


#4 

def reverseWord(text):
    result=''
    text=list(text)
    text.reverse()
    for i in text:
        result+=str(i)
    print(result)

#5
def writeoneline():
    print(f"Languanges: Python C JavaScript")


#6
def writeescape():
    print("\"Forever for now\" is one of the.")


#7
def writehalftext():
    text='O, ümumi PFA və FWA mükafatını alan ilk futbolçu oldu. 2008,2013,2014,2016-cü illərdə Qızıl top mükafatını qazandı.'  
    text=list(text)
    result=''
    for i in range(0,int(len(text)/2)):
        result+=text[i]
    print(result)

#8 
def writepower():
    x=2
    y=3

    xresult=x
    yresult=y

    for i in range(1,y):
        xresult=xresult*x
        
    
    for i in range(1,x):
        yresult=yresult*y

    print(xresult,yresult)


#10 
def findWord(word):
    text='Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function". Orwell like Marcel Proust fears that the habit of conforming to the force benumbs sensations and erases the perception of the world. Technological totalitarianism alienates senses, controls human behaviour and leads to linguistic degradation'
    text=text.split(' ')
    isFind=False
  
    for i in text:
        if word==i:
            isFind=True
    if isFind==True:
        return f"{word} tapildi"
    else:
        return 'tapilmadi'

# print(findWord('text'))

#11
def oddNumber():
    x=9
    if x<10 or x%2!=0:
        print('not okay')
    elif x>10 and x%2==0:
        print('okay')
    elif x<10 and x%2!=0:
        print('bad')
oddNumber()