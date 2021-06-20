import random

questionNum=0
true_q=0
false_q=0

def startGame():

    def showQuestion():
      
        num1=random.randrange(10,99)
        num2=random.randrange(10,99)
        total=num1+num2
        question=int(input(f'{num1}+{num2}='))
        global questionNum,true_q,false_q
        questionNum+=1
        
        if question==total:
            
            true_q+=1
            print('true')
        else:
            false_q+=1
            print('false')
            
        
        if questionNum<10:
            
            showQuestion()
        if questionNum==10:
            print('------------- results')
            print(f'true-{true_q}')
            print(f'false-{false_q}')

     
    showQuestion()

    
startGame()