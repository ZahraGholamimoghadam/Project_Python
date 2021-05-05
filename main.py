# This is a program for store system that was written by zahra.

from admin import Admin
from customer import Customer

print('\n\t\t\t\t\t\t\t\t\t******** Welcom to the store system *********')


# In this function we run methods corresponding to the customer based on user's choice.
def customer_interaction():
    while True:
        print('\n======Uer MENU=======\n1. Show products\n2. Shopping\n3. Logout')
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            Customer.show_products()
        elif choice == 2:
            lst1 = list(map(int, input("Enter the rows' numbers corresponding to products "
                                       "that you want to buy with specifying ',': ").split(',')))
            lst2 = list(map(int, input("Enter the number of selected products in order with specifying ',': ").split(',')))
            lst_input = list(zip(lst1, lst2))
            Customer.shopping(lst_input)
            Customer.update_inventory(lst_input)
        elif choice == 3:
            break


# In this function we run methods corresponding to the admin based on user's admin.
def admin_interaction():
    while True:
        print('\n======Admin MENU=======\n1. Add product\n2. Show invoices\n3. Logout')
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            info_product = input('Enter product specifications with specifying "," '\
            '(name,brand,price,barcode,inventory number): ').split(',')
            print(Admin.add_product(info_product))
        elif choice == 2:
            Admin.show_invoices()
        elif choice == 3:
            break


choice = 'y'
while choice == 'y':
    if input('\nAre you admin? ') == 'y':
        if int(input('Enter your security code:')) == 9797:
            if input('Do you have any account?(y/n) ') == 'n':
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                person = Customer(username, password)
                person.register()
                print(f'\n--> You have successfully registered.')
                Admin.checking_inventory()
                admin_interaction()
            else:
                person = Customer.login()
                if person:
                    print('\nWe confirmed that you are admin.\n')
                    Admin.checking_inventory()
                    admin_interaction()
        else:
            print('-->You are not admin!!')
    elif input('Doo you have any account?(y/n) ') == 'n':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        person = Customer(username, password)
        person.register()
        print(f'\n--> {username}, you have successfully registered.')
        customer_interaction()
    else:
        person = Customer.login()
        if person != False:
            customer_interaction()
    choice = input('\nDo you want to continue? (y/n): ')













