def topNum(num,top=1):
    staticNum=num
    for i in range(0,top):
        num=num*staticNum
    return num

print(topNum(5,2))
    