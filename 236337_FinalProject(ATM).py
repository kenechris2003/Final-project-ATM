# Importing necessary module(s)/libraries

from time import *  # To simulate loading time of an ATM


# Display bank name
print('\n                      WELCOME TO BLUE ONYX BANK \n    "Where Financial Stability Meets Personal Transformation"') 
sleep(3)

# Initializing / Creating Customers account 

Customer1_name = 'Kenechukwu Chris Chisom'
Customer1_acc_no = 1234567890
Customer1_Pin = 12345
Customer1_acct_bal = 200000

Customer2_name = 'Uche Henry Onyedikachukwu' 
Customer2_acc_no = 1111122222
Customer2_Pin = 12121
Customer2_acct_bal = 890000

Customer3_name = 'Osinaku Ugonna Slyvia'
Customer3_acct_no = 2233445566
Customer3_Pin = 23456
Customer3_acct_bal = 570000

# Trial count
trial = 2   # I used 2 here instead of 3 before i am already using a trial when i initialize the variable (account number/Pin)

# Account number / Pin Validation
account_no = 0
while len(str(account_no)) != 10:   # Validating user-inputted account number length 
    # I used str() in other to convert the account number which is a integer to a string so i can get the length
        account_no = input('Enter your account number: ')
        while account_no.isdecimal() is not True:   # Handling non-numeric input
            if trial == 2:
                print('You have', trial,'trial left')
            if trial == 1:
                print('You have', trial,'trial left')
            if trial == 0:
                print('Sorry we could not validate your account number, please try again later\nThanks for banking with us') 
                exit()
            else:
                print("Account number must be 10 digits")
                account_no = input('Enter your account number: ')
                trial -= 1
                sleep(1)
        
account_pin = 0
while len(str(account_pin)) != 5: # Validating user-inputted PIN length
    account_pin = input('Enter your pin: ')
    while account_pin.isdecimal() is not True:  # Handling non-numeric input
        if trial == 2:
            print('You have', trial,'trial left')
        if trial == 1:
            print('You have', trial,'trial left')
        if trial == 0:
            print('Sorry we could not validate your pin, please try again \nThanks for banking with us') 
            exit()
        else:
            print("Pin must be 5 digits")
            account_pin = input('Enter your pin: ')
            trial -= 1
            sleep(1)
            
account_pin = int(account_pin)  # I am converting the account number back to an integer in other to validate in with the already initialize account details
account_no = int(account_no)  # I am converting the account pin back to an integer in other to validate in with the already initialize account details

sleep(1)
print('Please wait......')
sleep(2)


#  Validating if the account details exist in the bank
if (account_no) == Customer1_acc_no and (account_pin) == Customer1_Pin:
    print('Pin validated......')
    sleep(1)
    print('Welcome',Customer1_name,',Which of the following transaction would you like to perform....') # Displaying a personalized welcome message for Customer1
    sleep(2)
elif (account_no) == Customer2_acc_no and (account_pin) == Customer2_Pin:
    print('Pin validated......')
    sleep(1)
    print('Welcome',Customer2_name,',Which of the following transaction would you like to perform....') # Displaying a personalized welcome message for Customer2
    sleep(2)
elif (account_no) == Customer3_acct_no and (account_pin) == Customer3_Pin:
    print('Pin validated......')
    sleep(1)
    print('Welcome',Customer3_name,',Which of the following transaction would you like to perform....') # Displaying a personalized welcome message for Customer3
    sleep(2)
else:
    print('Sorry, account infomation no found \n Kindly visit the bank to create an account......\n Thank you for Banking with us... \n We would love to see you again') # Handling case where entered account details don't match any customer
    exit()

print("")

# Displays the main menu options
print("*" *60)
# Displaying main menu options for the user to choose from
print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
print("")
print("*" *60)
sleep(2)

choice = input('Enter a choice: ')  # Handling user's choice for balance, withdrawal, deposit, or exit
while choice.isdecimal() is not True: # Handling non-numeric input
    print('Input must be a number')
    choice = input('Enter a choice: ')
print('')
sleep(2)


while True:
    # Balance display
    if int(choice) == 1:
        if account_pin == Customer1_Pin:
            print('Your balance is',Customer1_acct_bal, 'NAIRA') # Displaying balance 
            sleep(1)
            print('Would you like to perform another transaction? \n 1 - Yes   2 - No ')  # handling user's choice for another transaction    
            
            choice_2 = input('Enter a choice: ')
            while choice_2.isdecimal() is not True:  # Handling non-numeric input
                print('Input must be a number')
                choice_2 = input('Enter a choice: ')
            if int(choice_2) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                while choice.isdecimal() is not True:  # Handling non-numeric input
                    print('Input must be a number')
                    choice = input('Enter a choice: ')
                sleep(2)
            else:
                print('Thank you for banking with us \n We would love to see you again \n BYE!!!! for now')
                sleep(2)
                exit()   
            
        elif account_pin == Customer2_Pin:
            print('Your balance is',Customer2_acct_bal, 'NAIRA')
            sleep(1)
            print('Would you like to perform another transaction? \n 1 - Yes   2 - No ')
            
            choice_2 = input('Enter a choice: ')
            while choice_2.isdecimal() is not True:
                print('Input must be a number')
                choice_2 = input('Enter a choice: ')
            if int(choice_2) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                while choice.isdecimal() is not True:
                    print('Input must be a number')
                    choice = input('Enter a choice: ')
                sleep(2)
            else:
                print('Thank you for banking with us \nWe would love to see you again \nBYE!!!! for now')
                sleep(2)
                exit()  
        elif account_pin == Customer3_Pin:
            print('Your balance is',Customer3_acct_bal, 'NAIRA')
            sleep(1)
            print('Would you like to perform another transaction? \n 1 - Yes   2 - No ')
            
            choice_2 = input('Enter a choice: ')
            while choice_2.isdecimal() is not True:  # Handling non-numeric input
                print('Input must be a number')
                choice_2 = input('Enter a choice: ')
            if int(choice_2) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                while choice.isdecimal() is not True:
                    print('Input must be a number')
                    choice = input('Enter a choice: ')
                print('')
                sleep(2)
            else:
                print('Thank you for banking with us  \nWe would love to see you again \nBYE!!!! for now')
                sleep(2)
                exit()
                
    # Withdrawal Display
    elif int(choice) == 2:    
        while int(choice) == 2: # Handling user's choice for withdrawal amount
            print('Withdrawal menu\n  1 - 1000 Naira   4 - 10000 Naira\n  2 - 2000 Naira   5 - 20000 Naira\n  3 - 5000 Naira   6 - Other amount  7 - Cancel Transaction')
            withdrawal_choice = input('Choose a withdrawal amount: ') # Handling user's choice for specific withdrawal amount 
            while withdrawal_choice.isdecimal() is not True: # Handling non-numeric input
                print('Input must be a number')
                withdrawal_choice = input('Enter a choice: ')
            print('')
            if int(withdrawal_choice) == 1:
                if account_pin == Customer1_Pin:
                    if Customer1_acct_bal >= 1000:
                        new_balance_1 = (Customer1_acct_bal - 1000)
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_1)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_2)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_3)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_1)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_2)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_3)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_1)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_2)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_3)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_1)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_2)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_3)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_1)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_2)
                        print('')
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
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_3)
                        print('')
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
            elif int(withdrawal_choice) == 6:
                if account_pin == Customer1_Pin:
                    Other_amount = input('Enter the amount: ')
                    while Other_amount.isdecimal() is not True:
                        print('Input must be a number')
                        Other_amount = input('Enter a choice: ')
                    if Customer1_acct_bal >= int(Other_amount):
                        new_balance_1 = (Customer1_acct_bal - int(Other_amount))
                        Customer1_acct_bal = new_balance_1
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_1)
                        print('')
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
                elif account_pin == Customer2_Pin:
                    if Customer2_acct_bal >= int(Other_amount):
                        new_balance_2 = (Customer2_acct_bal - int(Other_amount))
                        Customer2_acct_bal = new_balance_2
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_2)
                        print('')
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break 
                elif account_pin == Customer3_Pin:
                    if Customer3_acct_bal >= int(Other_amount):
                        new_balance_3 = (Customer3_acct_bal - int(Other_amount))
                        Customer3_acct_bal = new_balance_3
                        sleep(0.5)
                        print('Transaction in Progress..... Please wait.....')
                        sleep(3)
                        print('Withdrawal Successful......')
                        sleep(1)
                        print('Your balance is',new_balance_3)
                        print('')
                        sleep(1)
                    else:
                        print('Insufficient Funds')
                        break
            else:
                print('Please wait....')
                sleep(1)
                print('Withdrawal Transaction Cancelled.....')
                sleep(0.5)
                print('No amount deducted')
                sleep(1)
                if account_pin == Customer1_Pin:
                    print('Your balance is',Customer1_acct_bal)
                elif account_pin == Customer2_Pin:
                    print('Your balance is',Customer2_acct_bal)
                elif account_pin == Customer3_Pin:
                    print('Your balance is',Customer3_acct_bal)
                break
        
        print('\n Would you like to perform any another transaction?\n 1 - Yes   2 - No ') # Handling user's choice for another transaction after all withdrawals

        choice_3 = input('Enter a choice: ')
        while choice_3.isdecimal() is not True:
            print('Input must be a number')
            choice_3 = input('Enter a choice: ')
        
        if int(choice_3) == 1:
            print("*" *60)
            print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
            print("*" *60)
            sleep(2)
            choice = input('Enter a choice: ')
            while choice.isdecimal() is not True:
                print('Input must be a number')
                choice = input('Enter a choice: ')
            sleep(2)

        elif int(choice_3) == 2:
            sleep(0.5)
            print('Thank you for banking with us \n We would love to see you again \n BYE!!!! for now')
            sleep(2)
            exit()
            
    # Deposit Menu
    elif int(choice) == 3:
        print("")
        print('Maximum Deposit is 1000000 \n Press 0 to terminate transaction')
        deposit_choice = input('Enter a deposit amount: ')
        while deposit_choice.isdecimal() is not True:
            print('Input must be a number')
            deposit_choice = input('Enter a choice: ')
        print("")
        deposit_choice = int(deposit_choice)
        if deposit_choice == 0:  # Handling user's choice to terminate deposit transaction
            sleep(1)
            print('Please Wait......')
            sleep(1.5)
            print('Deposit transaction Terminated')
            sleep(2)
            
            print('\n Would you like to perform any another transaction?\n 1 - Yes   2 - No ')  # Handling user's choice for another transaction after terminating deposit
            
            choice_4 = input('Enter a choice: ')
            while choice_4.isdecimal() is not True:
                print('Input must be a number')
                choice_4 = input('Enter a choice: ')
            
            if int(choice_4) == 1:
                print("*" *60)
                print('Main menu\n  1 - View my balance\n  2 - Withdraw cash\n  3 - Deposit funds\n  4 - Exit')
                print("*" *60)
                sleep(2)
                choice = input('Enter a choice: ')
                while choice.isdecimal() is not True:
                    print('Input must be a number')
                    choice = input('Enter a choice: ')
                sleep(2)
                
            
            elif int(choice_4) == 2:
                sleep(1)
                print('Thank you for banking with us \n We would love to see you again \n BYE!!!! for now')
                sleep(2)
                exit()

        elif deposit_choice <= 1000000:
            if account_pin == Customer1_Pin:
                sleep(0.5)
                print('Transaction in Progress..... Please wait.....')
                sleep(3)
                print('Deposit Successful......')
                sleep(1)
                new_balance_deposit_1 = Customer1_acct_bal + deposit_choice
                print('Your balance is',new_balance_deposit_1)
                Customer1_acct_bal = new_balance_deposit_1
            elif account_pin == Customer2_Pin:
                sleep(0.5)
                print('Transaction in Progress..... Please wait.....')
                sleep(3)
                print('Deposit Successful......')
                sleep(1)
                new_balance_deposit_2 = Customer2_acct_bal + deposit_choice
                print('Your balance is',new_balance_deposit_2)
                Customer2_acct_bal = new_balance_deposit_2
            elif account_pin == Customer3_Pin:
                sleep(0.5)
                print('Transaction in Progress..... Please wait.....')
                sleep(3)
                print('Deposit Successful......')
                sleep(1)
                new_balance_deposit_3 = Customer3_acct_bal + deposit_choice
                print('Your balance is',new_balance_deposit_3)
                Customer3_acct_bal = new_balance_deposit_3
                
    # Exit Program
    elif int(choice) == 4:
            sleep(1)
            print('Thank you for banking with us \n We would love to see you again \n BYE!!!! for now')   # Displaying exit message and terminating the program
            sleep(2)
            exit()  
                 