#1
def sumlist():
    lis=[4,56,78,90]
    result=0
    for i in lis:
        result+=i

    print(result)

#2
def multplylist():
    lis=[8, 2, 3, -1, 7]
    result=1
    for i in lis:
        result*=i
    print(result)


#3 
def returnDay(d):
    day=int(d)
    days=[
        {
            "day":1,
            "weekday":"monday"
        },
        {
            "day":2,
            "weekday":"tuedsday"
        },
        {
            "day":3,
            "weekday":"wednesday"
        },
        {
            "day":4,
            "weekday":"thursday"
        },
        {
            "day":5,
            "weekday":"firday"
        },
        {
            "day":6,
            "weekday":"saturday"
        }
        ,{
            "day":7,
            "weekday":"sunday"
        }

    ]
    if day>len(days) or day<1:
        return None
    
    else:
        for i in days:
            if day==i['day']:
                return i['weekday']


print(returnDay(8))