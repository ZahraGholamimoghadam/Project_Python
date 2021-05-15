import csv
import hashlib
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG,filename='store_logs.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')


class Customer:
    def __init__(self, username, password):
        """
        :param username: username of customer
        :param password: password of customer
        """
        self.username = username
        self.password = password.encode()

    def register(self):
        with open('accounts.csv', 'r+', newline='') as file:
            lst = list(csv.reader(file))
            usernames = [row[0] for row in lst if row]
            if self.username not in usernames:
                writer_accounts = csv.DictWriter(file, fieldnames=['usr', 'pass', 'status'])
                writer_accounts.writerow({'usr': self.username, 'pass': hashlib.sha256(self.password).hexdigest(), 'status':1})
                return True
            else:
                return False

    @staticmethod
    def changing_status(username):
        """
        In this function we unblock the blocked users.
        """
        try:
            with open('accounts.csv') as f:
                df = pd.read_csv(f)
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            df.loc[df['usr'] == username, 'status'] = 0
            df.to_csv("accounts.csv", index=False)

    def login(self):
        try:
            with open("accounts.csv") as file:
                flg = False
                existing_rows = list(csv.reader(file))
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            if [self.username, hashlib.sha256(self.password).hexdigest(), '0'] in existing_rows:
                print('\nYour account is already locked.')
            else:
                for i in range(2):
                    if [self.username, hashlib.sha256(self.password).hexdigest(), '1'] in existing_rows:
                        print('\n-->Your login was successful.')
                        flg = True
                        break
                    else:
                        self.password = input('Enter your password: ').encode()
                else:
                    print('\n--> Your account was locked!')
                    Customer.changing_status(self.username)

            return flg

    @staticmethod
    def show_products():
        try:
            df = pd.read_csv("products.csv")
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            df1 = df[['name', 'price', 'brand']]
            print('        --------List of products available in the store is as follows:--------\n')
            print(df1)

    @staticmethod
    def create_invoice(username, lst_orders):
        with open("invoices.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'purchased number', 'total price', "customer's name"])
            writer.writerows(lst_orders)
            logging.info(f'A new invoice was created for {username}')

    @staticmethod
    def billing(lst_orders):
        total = 0
        for i in lst_orders:
            total += i['total price']
        print(f'\n--->The final price of your purchase is: {total} Toman')

    @staticmethod
    def shopping(lst_inputs, username):
        lst_orders = []
        try:
            with open("products.csv") as file:
                reader = list(csv.DictReader(file))
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            for i in range(len(lst_inputs)):
                row_number = lst_inputs[i][0]
                if int(reader[row_number]['inventory number']) >= lst_inputs[i][1]:
                    lst_orders.append({'name': reader[row_number]['name'], 'price': reader[row_number]['price'],
                                      'purchased number': lst_inputs[i][1],
                                      'total price': int(reader[row_number]['price']) * lst_inputs[i][1],
                                      "customer's name": username})
                else:
                    print(f'\nInventory of {reader[row_number]["name"]} is {reader[row_number]["inventory number"]}'
                          f' that is less than the number you requested.')
            Customer.create_invoice(username, lst_orders)
            Customer.billing(lst_orders)

    @staticmethod
    def update_inventory(lst_input):
        try:
            df = pd.read_csv("products.csv")
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            for i in range(len(lst_input)):
                # updating the column value
                df.loc[lst_input[i][0], 'inventory number'] -= lst_input[i][1]
                # writing into the file
                df.to_csv("products.csv", index=False)














