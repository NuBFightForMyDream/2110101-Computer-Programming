76# Case-Scenario 1 : Guessing Number by Input Number (Define Start-End By Myself) (Using Bisection Idea)

# 1 : define start & end & input guess number
start = int(input('Enter Start Guessing Number Range : '))
end = int(input('Enter End Guessing Number Range : '))
winner = False # check if guess right number

# 2 : structure of program
import random
real_num = random.randint(start , end)

round_left = 10 
print(f"Guessing Number from {start} to {end}")

for round_left in range(9,-1,-1) : # rp = round passed (start from 9 to 0)
    # Enter Guess Number
    guess_num = int(input('Guessing Number : '))
    
    # case 1 : guess_num > real_num : tell user for lower number (dont forget to change start & end number)
    if guess_num > real_num : 
        print(f"{guess_num} is higher than real number , Input Lower Number")
        
        # change end (if new guess is less than end)
        if guess_num < end : 
            end = guess_num - 1
    
    # case 2 : guess_num < real_num : tell user for higher number (dont forget to change start & end number)
    elif guess_num < real_num : 
        print(f"{guess_num} is lower than real number , Input Higher Number")
        
        # change start (if new guess is more than start)
        if guess_num > start : 
            start = guess_num + 1
        
    # case 3 : same number -> break
    elif guess_num == real_num :
        winner = True
        print(f'Congratulations , You Guesses Right . The Real Number is {real_num}')
        break
    
    # still input new number
    print(f"Round Left #{round_left} : Guessing Number from {start} to {end}")
    
# check winner
if winner == False : 
    print('Bad Luck , Try Again Next Time . Real Number is' , real_num)