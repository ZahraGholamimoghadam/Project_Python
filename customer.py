import csv
import hashlib
import pandas as pd


class Customer:
    def __init__(self, username, password):
        """
        :param username: username of customer
        :param password: password of customer
        """
        self.username = username
        self.password = password.encode()

    def register(self):
        with open('accounts.csv', 'a', newline='') as file_accounts:
            writer_accounts = csv.DictWriter(file_accounts, fieldnames=['usr', 'pass'])
            writer_accounts.writerow({'usr': self.username, 'pass': hashlib.sha256(self.password).hexdigest()})

    @staticmethod
    def login():
        person = False
        with open("accounts.csv") as file:
            existing_rows = list(csv.reader(file))
            for i in range(3):
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                if [username, hashlib.sha256(password.encode()).hexdigest()] in existing_rows:
                    print('\n-->Your login was successful.')
                    person = Customer(username, password)
                    break
            else:
                print('\n--> Your account was locked!')

        return person


    @staticmethod
    def show_products():
        with open("products.csv") as file:
            df = pd.read_csv(file)
            print('        --------List of products available in the store is as follows:--------\n')
            print(df)


    @staticmethod
    def shopping(lst_inputs):
        lst_orders = []
        with open("products.csv") as file:
            reader = list(csv.DictReader(file))
            # print(reader)
            for i in range(len(lst_inputs)):
                j = lst_inputs[i][0]
                lst_orders.append({'name': reader[j]['name'], 'price': reader[j]['price'],
                                  'purchased number': lst_inputs[i][1],
                                  'total price': int(reader[j]['price']) * lst_inputs[i][1]})

        with open("invoices.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'purchased number', 'total price'])
            writer.writerows(lst_orders)
        total = 0
        for i in lst_orders:
            total += i['total price']
        print(f'\n--->The final price of your purchase is: {total} Toman')


    @staticmethod
    def update_inventory(lst_input):
        df = pd.read_csv("products.csv")
        for i in range(len(lst_input)):
            # updating the column value
            df.loc[lst_input[i][0], 'inventory number'] -= lst_input[i][1]
            # writing into the file
            df.to_csv("products.csv", index=False)













