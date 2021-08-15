print("Welcome to the Dease ATM")
restart = 'Y'
chances = 3
balance = 1502
while chances >= 0:
    pin = int(input('Please Enter Your 4 digit pin: '))
    if pin == 9870:
        print('You entered pin correctly')
        print('Please Press 1 For Your Balance')
        print('Please Press 2 To Make a Withdrawal')
        print('Please Press 3 To Pay in')
        print('Please Press 4 To Return Card\n')
        while restart not in ('n', 'NO', 'N', 'no'):
            print('Please Press 1 For Your Balance')
            print('Please Press 2 To Make a Withdrawal')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')
            option = int(input('What would you like to choose'))
            if option == 1:
                print("Your Balance is", balance)
                restart = input('Would You Like To Go Back?')
                if restart in('n', 'NO', 'N', 'no'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = 'y'
                withdrawl = float(input('How Much Would You Like To Withdraw,
                                10, 20, 40, 60, 80, 100 for other enter 1: '))

if withdrawal in[10, 20, 40, 60, 80, 100]:
            balance = balance - withdrawal
            print('\nYour Balance is now, balance)
            restart = input('Would You like to go back?')
            if restart in('n', 'NO', 'N', 'no'):
                print('Thank You ')
            break

