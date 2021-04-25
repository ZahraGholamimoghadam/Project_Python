# This is a program for store system that was written by zahra.

from admin import Admin
from customer import Customer

print('\n\t\t\t\t\t\t\t\t\t******** Welcom to the store system *********')


def customer_interaction(person):
    print('\n======Uer MENU=======\n1. Show product\n2. Shopping\n3. Exit')
    choice = int(input("\nEnter Choice: "))
    while choice != 3:
        if choice == 1:
            print(person.show_products())
        elif choice == 2:
            print(person.shopping())
        print('\n======Uer MENU=======\n1. Show product\n2. Shopping\n3. Exit')
        choice = int(input("\nEnter Choice: "))


# In this function we run methods corresponding to the customer based on user's choice.
def admin_interaction(admin):
    print('\n======Admin MENU=======\n1. Create product\n2. Show invoices\n3. Exit')
    choice = int(input("\nEnter Choice: "))
    while choice != 3:
        if choice == 1:
            print(admin.create_product())
        elif choice == 2:
            print(admin.show_invoices())
        print('\n======Admin MENU=======\n1. Create product\n2. Show invoices\n3. Exit')
        choice = int(input("\nEnter Choice: "))


# In this function we run methods corresponding to the admin based on user's admin.
if input('\nAre you admin? ') == 'y':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == 'zahra' and password == '1335':
        admin = Admin(username, password)
        print('\n--> We confirmed that you are admin.')
        admin_interaction(admin)
    else:
        print('-->You are not admin!')

elif input('Do you have any account?(y/n) ') == 'n':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    person = Customer(username, password)
    person.register()
    print(f'\n--> {username}, you have successfully registered.')
    customer_interaction(person)

else:
    person = Customer.login()
    if person != False:
        customer_interaction(person)












