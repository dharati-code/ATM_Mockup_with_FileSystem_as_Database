# Author : Dharatiben Shah

# imports 
import random
import database 
from getpass import getpass
import validation


user_account_number = None # initalize as none 

def init():
    print(f"****** Welcome to bankPHP *******")

    have_account = int(
        input("Do you have an account with us ? Select 1(yes), 2(No) \n")
    )

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print(
            f"You have selected - {have_account} which is NOT a valid option ! Try again"
        )
        init()

def login():
    print("********* Login ***********")

    global account_number_from_user 
    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")
        global user
        user = database.authenticated_user(account_number_from_user, password);
        
        if user:
            is_auth_success = database.auth_create(account_number_from_user)
            if is_auth_success:
                bank_operation(user)
            

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()

def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation(account_number_from_user)
    elif selected_option == 2:

        withdrawal_operation(account_number_from_user)
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        final_exit()
    else:

        print("Invalid option selected")
        bank_operation(user)

def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print(f"Your account number is: {account_number}")
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()

def withdrawal_operation(account_number_from_user):
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance
    current_balance = int(get_current_balance(account_number_from_user))
    amount_to_withdraw = input("How much do you want to withdraw? \n")
    if current_balance >= int(amount_to_withdraw):
        final_balance = current_balance-int(amount_to_withdraw)
        if database.update(account_number_from_user,str(final_balance)):
            print(f"Success ! Your new balance is {final_balance}")
            bank_operation(user)
    else:
        print(f"Invalid transaction : You asked to withdraw $ {amount_to_withdraw} but your current balance is : $ {current_balance}")
        bank_operation(user)

def deposit_operation(account_number_from_user):
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance
    
    current_balance = int(get_current_balance(account_number_from_user))
    amount_to_deposit = input("How much do you want to deposit? ")
    final_balance = current_balance+int(amount_to_deposit)

    if database.update(account_number_from_user,str(final_balance)):
        print(f"Your new account balance is {final_balance}")
        bank_operation(user)
    
    else:
        print("Transaction not successful")
        bank_operation(user)




def generation_account_number():
    return random.randrange(1111111111, 9999999999)



def get_current_balance(account_number_from_user):
    read_out = database.read(account_number_from_user).split(',')
    balance = read_out[4]
    print(f"The current balance for {account_number_from_user} is $ {balance}")
    return balance


def logout():
    # delete the file from the auth_session folder
    database.auth_delete(account_number_from_user)
    login()

def final_exit():
    # delete the file from auth_session folder since we exit out of program
    database.auth_delete(account_number_from_user)
    exit()

init()