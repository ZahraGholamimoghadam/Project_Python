# This is a program for store system that was written by zahra.

from admin import Admin
from customer import Customer
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG,filename='store_logs.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')

print('\n\t\t\t\t\t\t\t\t\t******** Welcom to the store system *********')


# In this function we run methods corresponding to the customer based on user's choice.
def customer_interaction(username):
    while True:
        try:
            print('\n======Uer MENU=======\n1. Show products\n2. Shopping\n3. Logout')
            choice = int(input("\nEnter your choice: "))
            assert (choice in [1, 2, 3])
            if choice == 1:
                Customer.show_products()
            elif choice == 2:
                Customer.show_products()
                lst1 = list(map(int, input("Enter the rows' numbers corresponding to products "
                                           "that you want to buy with specifying ',': ").split(',')))
                lst2 = list(map(int, input("Enter the number of selected products in order with specifying ',': ").split(',')))
                lst_input = list(zip(lst1, lst2))
                Customer.shopping(lst_input, username)
                Customer.update_inventory(lst_input)
            elif choice == 3:
                break
        except AssertionError:
            print('\nYour input is incorrect, please try again.')
            logging.error('Your input is incorrect, please try again.')
        except ValueError:
            print('\nYour input is incorrect, please try again.')
            logging.error('Your input is incorrect, please try again.')


# In this function we run methods corresponding to the admin based on user's admin.
def admin_interaction():
    while True:
        try:
            print('\n======Admin MENU=======\n1. Add product\n2. Show invoices\n3. Unblocking the blocked users'
                  '\n4. Logout')
            choice = int(input("\nEnter your choice: "))
            assert (choice in [1, 2, 3, 4])
            if choice == 1:
                info_product = input('Enter product specifications with specifying "," '\
                '(name,brand,price,barcode,inventory number): ').split(',')
                Admin.add_product(info_product)
                logging.info(f'{info_product[0]} was added to the store.')
            elif choice == 2:
                Admin.show_invoices()
            elif choice == 3:
                df = pd.read_csv('accounts.csv')
                df1 = df.loc[df['status'] == 0]
                df2 = df1.filter(['usr'])
                print(f'\n The following users have been blocked:\n{df2}\n')
                username = input('Which user do you want to unblock?(enter corresponding user: ')
                Admin.unblocking(username)
            elif choice == 4:
                break
        except AssertionError:
            print('\nYour input is incorrect, please try again.')
            logging.error('Your input is incorrect, please try again.')
        except ValueError:
            print('\nYour input is incorrect, please try again.')
            logging.error('Your input is incorrect, please try again.')


choice = 'y'
while choice == 'y':
    if input('\nAre you admin? ') == 'y':
        if input('Do you have any account?(y/n) ') == 'n':
            if input('Enter your security code: ') == '9797':
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                person = Customer(username, password)
                person.register()
                print(f'\n--> You have successfully registered.')
                Admin.checking_inventory()
                admin_interaction()
            else:
                print('-->Wrong security code!')
        else:
            person = Customer(input('Enter your username: '), input('Enter your password: '))
            if person.login():
                logging.info('Admin logged to system.')
                print('\nWe confirmed that you are admin.\n')
                Admin.checking_inventory()
                admin_interaction()

    elif input('Do you have any account?(y/n) ') == 'n':
        person = Customer(input('Enter your username: '), input('Enter your password: '))
        if person.register():
            print(f'\n--> You have successfully registered.')
            person = Customer(input('\nEnter your username: '), input('Enter your password: '))
            if person.login():
                customer_interaction(person.username)
        else:
            # raise Exception("\nThis username has already been used and isn't valid!")
            print("\nThis username has already been used and isn't valid!")
    else:
        person = Customer(input('Enter your username: '), input('Enter your password: '))
        if person.login():
            customer_interaction(person.username)
    choice = input('\nDo you want to continue? (y/n): ')











