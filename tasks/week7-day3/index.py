def start():
    total=0
    percentage=0
    lessons=[

        {
            'name':'english',
            "lesson":int(input('write your english mark '))
        },
     
        {
            'name':'phyiscs',
            "lesson":int(input('write your physic mark '))
        },
       
        {
            'name':'math',
            "lesson":int(input('write your math mark '))
        },
        
        {
            'name':'biology',
            "lesson":int(input('write your bio mark '))
        }
        
        ]
    print('---------------------------------------------')
    for i in lessons:
        
        if  i["lesson"]<=50:
            print(f'{i["name"]} grade is F')
        
        else:
            
            if i["lesson"]>50 and i['lesson']<=60:
                print(f'{i["name"]} grade is E')
            
            
            if i["lesson"]>60 and i["lesson"]<=70 :
                    print(f'{i["name"]} grade is D')

                
            if i["lesson"]>70 and i["lesson"]<=80:
                     print(f'{i["name"]} grade is C')

            if i["lesson"]>80 and i["lesson"]<=90:
                    print(f'{i["name"]} grade is B')

            if i["lesson"]>90:
                          print(f'{i["name"]} grade is A')

        total+=i["lesson"]

    
    print('-------------------------------------------------------------')
    print(f'total mark 400')
    print(f'your mark {total}')
    percentage=(total/400)*100
    print(percentage)

    
    if  percentage<50:
            print(f'your grade is F')
        
    else:
            
            if percentage>50 and i['lesson']<=60:
                print(f'your grade is E')
            
            
            if percentage>60 and percentage<=70 :
                    print(f'your grade is D')

                
            if percentage>70 and percentage<=80:
                     print(f'your grade is C')

            if percentage>80 and percentage<=90:
                    print(f'your grade is B')

            if percentage>90:
                          print(f'your grade is A')


start()


    




