import random
def Guess():  
    r=random.randint(1,100)    
    for I in range(1,11):     
        print(f'\n  GUESS NO. {I}')
        guess=input('  ENTER YOUR GUESS  : ')
        if guess=='Q':
            print('  YOU QUIT THE GAME')
            break     
        elif I ==10 and r !=guess:
            print('  YOU LOSE') 
            break   
        elif not guess.isdigit():
            print('  PLEASE ENTER ONLY NUMBERS\n')
            break
        guess=int(guess)
        if r<guess :
            print ('  HINT : ENTER SMALLER NUMBER  \n')     
        elif r>guess:
            print('  HINT : ENTER BIGGER NUMBER \n')   
      
        elif  r==guess:
            print('  YOU WON !')
            if I==1:
                print('  YOU ARE AN ALIEN : 👽')
            elif 1<I<=5:
                print('  YOU ARE FUTURE PREDICTOR ')
            elif 5<I<=10:
                print('  YOU ARE AMAZING ')
            break
       
        else:
            print('ENTER VALID NUMBER ')
             
        
    
    
print(''' ____________ =: GAME RULES := ____________\n\n 1. YOU HAVE TO GUESS A NUMBER BETWEEN 1-100.\n \n 2. YOU HAVE ONLY TEN GUESSES. \n \n 3. ENTER "Q" FOR QUIT THE GAME. \n''')    
s=input('  ENTER "S" FOR START THE GAME : ')
if s=='S':
    Guess()     

while True:
    rest=input('\n  ENTER "R" FOR RESTART ,  \n "Q" FOR QUIT THE GAME : ')
    if rest=='R':
        Guess()
    else:
        break 