# importting necessary module(s)/libraries

from time import *   # I used this library in other to be able to slow the the speed of the program, in other to simulate the loading time of an ATM

# Naming of my bank
print('\n                      WELCOME TO BLUE ONYX BANK \n    "Where Financial Stability Meets Personal Transformation"')
sleep(3)

# Intializing / Creating Customers account 

Customer1_name = 'Kenechukwu Chris Chisom'
Customer1_acc_no = 1234567890
Customer1_Pin = 12345
Customer1_acct_bal = 200000

Customer2_name = 'Uche Henry Onyedikachukwu' 
Customer2_acc_no = 1111122222
Customer2_Pin = 12121
Customer2_acct_bal = 890000

Customer3_name = 'Aderonke Sakpere'
Customer3_acct_no = 2233445566
Customer3_Pin = 23456
Customer3_acct_bal = 570000

# Trial count
trial = 2   # I used 2 here instead of 3 before i am already using a trial when i initialize the variable (account number/Pin)

account_no = int(input('Enter your account number: '))
sleep(1)

# Account number / Pin Validation

while len(str(account_no)) != 10:    # I used str() in other to convert the account number which is a integer to a string so i can get the length
    if trial == 0:
        print('Sorry we could not validate your account number, please try again later\nThanks for banking with us') 
        exit()
    else:
        print("Account number must be 10 digits")
        account_no = int(input('Enter your account number: '))
        trial -= 1
        sleep(1)
        
account_pin = int(input('Enter your pin: '))

while len(str(account_pin)) != 5:
    if trial == 0:
        print('Sorry we could not validate your pin, please try again \nThanks for banking with us') 
        exit()
    else:
        print("Pin must be 5 digits")
        account_pin = int(input('Enter your pin: '))
        trial -= 1
        sleep(1)

sleep(1)
print('Please wait......')
sleep(2)

#  Validating if the account details exist in the bank
if account_no == Customer1_acc_no and account_pin == Customer1_Pin:
    print('Pin validated......')
    sleep(1)
    print('Welcome',Customer1_name,',Which of the following transaction would you like to perform....')
    sleep(2)
elif account_no == Customer2_acc_no and account_pin == Customer2_Pin:
    print('Pin validated......')
    sleep(1)
    print('Welcome',Customer2_name,',Which of the following transaction would you like to perform....')
    sleep(2)
elif account_no == Customer3_acct_no and account_pin == Customer3_Pin:
    print('Pin validated......')
    sleep(1)
    print('Welcome',Customer3_name,',Which of the following transaction would you like to perform....')
    sleep(2)
else:
    print('Sorry, account infomation no found')
    exit()

print("")

# Main Menu display
print("*" *60)
print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
print("")
print("*" *60)
sleep(2)
choice = input('Enter a choice: ')
sleep(2)


while True:
    # Balance display
    if int(choice) == 1:
        if account_pin == Customer1_Pin:
            print('Your balance is',Customer1_acct_bal, 'NAIRA')
            sleep(1)
            print('Would you like to perform another transaction? \n 1 - Yes   2 - No ')
            
            choice_2 = input('Enter a choice: ')
            if int(choice_2) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                sleep(2)
            else:
                print('Thank you for banking with us')
                sleep(2)
                exit()   
            
        elif account_pin == Customer2_Pin:
            print('Your balance is',Customer2_acct_bal, 'NAIRA')
            sleep(1)
            print('Would you like to perform another transaction? \n 1 - Yes   2 - No ')
            
            choice_2 = input('Enter a choice: ')
            if int(choice_2) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                sleep(2)
            else:
                print('Thank you for banking with us')
                sleep(2)
                exit()  
        elif account_pin == Customer3_Pin:
            print('Your balance is',Customer3_acct_bal, 'NAIRA')
            sleep(1)
            print('Would you like to perform another transaction? \n 1 - Yes   2 - No ')
            
            choice_2 = input('Enter a choice: ')
            if int(choice_2) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                sleep(2)
            else:
                print('Thank you for banking with us')
                sleep(2)
                exit()
                
    # Withdrawal Display
    elif int(choice) == 2:    
        while int(choice) == 2: 
            print('Withdrawal menu\n  1 - 1000 Naira   4 - 10000 Naira\n  2 - 2000 Naira   5- 20000 Naira\n  3 - 5000 Naira   6- Cancel transaction')
            withdrawal_choice = input('Choose a withdrawal amount: ') 
            if int(withdrawal_choice) == 1:
                if account_pin == Customer1_Pin:
                    if Customer1_acct_bal >= 1000:
                        new_balance_1 = (Customer1_acct_bal - 1000)
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_1)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                        
                elif account_pin == Customer2_Pin:
                    if Customer2_acct_bal >= 1000:
                        new_balance_2 = (Customer2_acct_bal - 1000)
                        Customer2_acct_bal = new_balance_2
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_2)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break 
                elif account_pin == Customer3_Pin:
                    if Customer3_acct_bal >= 1000:
                        new_balance_3 = (Customer3_acct_bal - 1000)
                        Customer2_acct_bal = new_balance_3
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_3)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
            elif int(withdrawal_choice) == 2:
                if account_pin == Customer1_Pin:
                    if Customer1_acct_bal >= 2000:
                        new_balance_1 = (Customer1_acct_bal - 2000)
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_1)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer2_Pin:
                    if Customer2_acct_bal >= 2000:
                        new_balance_2 = (Customer2_acct_bal - 2000)
                        Customer2_acct_bal = new_balance_2
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_2)
                        sleep(1) 
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer3_Pin:
                    if Customer3_acct_bal >= 2000:
                        new_balance_3 = (Customer3_acct_bal - 2000)
                        Customer3_acct_bal = new_balance_3
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_3)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                    
            elif int(withdrawal_choice) == 3:
                if account_pin == Customer1_Pin:
                    if Customer1_acct_bal >= 5000:
                        new_balance_1 = (Customer1_acct_bal - 5000)
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_1)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer2_Pin:
                    if Customer2_acct_bal >= 5000:
                        new_balance_2 = (Customer2_acct_bal - 5000)
                        Customer2_acct_bal = new_balance_2
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_2)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                    
                elif account_pin == Customer3_Pin:
                    if Customer3_acct_bal >= 5000:
                        new_balance_3 = (Customer3_acct_bal - 5000)
                        Customer3_acct_bal = new_balance_3
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_3)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
            elif int(withdrawal_choice) == 4:
                if account_pin == Customer1_Pin:
                    if Customer1_acct_bal >= 10000:
                        new_balance_1 = (Customer1_acct_bal - 10000)
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_1)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer2_Pin:
                    if Customer2_acct_bal >= 10000:
                        new_balance_2 = (Customer2_acct_bal - 10000)
                        Customer2_acct_bal = new_balance_2
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_2)
                        sleep(1) 
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer3_Pin:
                    if Customer3_acct_bal >= 10000:
                        new_balance_3 = (Customer3_acct_bal - 10000)
                        Customer3_acct_bal = new_balance_3
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_3)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                    
            elif int(withdrawal_choice) == 5:
                if account_pin == Customer1_Pin:
                    if Customer1_acct_bal >= 20000:
                        new_balance_1 = (Customer1_acct_bal - 20000)
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_1)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer2_Pin:
                    if Customer2_acct_bal >= 20000:
                        new_balance_2 = (Customer2_acct_bal - 20000)
                        Customer2_acct_bal = new_balance_2
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_2)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break 
                elif account_pin == Customer3_Pin:
                    if Customer3_acct_bal >= 20000:
                        new_balance_3 = (Customer3_acct_bal - 20000)
                        Customer3_acct_bal = new_balance_3
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(1.5)
                        print('Withdrawal Successful......')
                        sleep(0.5)
                        print('Your balance is',new_balance_3)
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
            else:
                print('Withdrawal Transaction Cancelled.....')
                print('No amount deducted')
                if account_pin == Customer1_Pin:
                    print('Your balance is',new_balance_1)
                elif account_pin == Customer2_Pin:
                    print('Your balance is',new_balance_2)
                elif account_pin == Customer3_Pin:
                    print('Your balance is',new_balance_3)
                print('\n Would you like to perform another transaction?\n 1 - Yes   2 - No ')
                
                choice_3 = input('Enter a choice: ')
                
                if int(choice_3) == 1:
                        print("*" *60)
                        print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                        print("*" *60)
                        sleep(2)
                        choice = input('Enter a choice: ')
                        sleep(2)
                        continue
                        
                elif int(choice_3) == 2:
                        sleep(0.5)
                        print('Thank you for banking with us')
                        sleep(2)
                        exit()

        print('\n Would you like to perform any another transaction?\n 1 - Yes   2 - No ')

        choice_4 = input('Enter a choice: ')
        
        if int(choice_4) == 1:
            print("*" *60)
            print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
            print("*" *60)
            sleep(2)
            choice = input('Enter a choice: ')
            sleep(2)

        elif int(choice_4) == 2:
            sleep(0.5)
            print('Thank you for banking with us')
            sleep(2)
            exit()
            
    # Deposit Menu
    elif int(choice) == 3:
        print("")
        print('Maximum Deposit is 1000000 \n Press 0 to terminate transaction')
        deposit = int(input('Enter a deposit amount: '))
        print("")
        if deposit == 0:
            sleep(0.5)
            print('Thank you for banking with us')
            sleep(2)
            exit()
        elif deposit <= 1000000:
            if account_pin == Customer1_Pin:
                new_balance_deposit_1 = Customer1_acct_bal + deposit
                print('Your balance is',new_balance_deposit_1)
                Customer1_acct_bal = new_balance_deposit_1
            elif account_pin == Customer2_Pin:
                new_balance_deposit_2 = Customer2_acct_bal + deposit
                print('Your balance is',new_balance_deposit_2)
                Customer2_acct_bal = new_balance_deposit_2
            elif account_pin == Customer3_Pin:
                new_balance_deposit_3 = Customer3_acct_bal + deposit
                print('Your balance is',new_balance_deposit_3)
                Customer3_acct_bal = new_balance_deposit_3
                
    # Exit Program
    elif int(choice) == 4:
            sleep(0.5)
            print('Thank you for banking with us')
            sleep(2)
            exit()  
                 