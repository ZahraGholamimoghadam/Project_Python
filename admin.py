import csv
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG,filename='store_logs.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')


class Admin:
    def __init__(self, username, password):
        """
        :param username: username of customer
        :param password: password of customer
        """
        self.username = username
        self.password = password.encode()

    @staticmethod
    def add_product(info_product):
        with open("products.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(info_product)

    @staticmethod
    def show_invoices():
        try:
            with open("invoices.csv") as file:
                df = pd.read_csv(file)
        except FileNotFoundError as e:
            print(e)
        else:
            if df.empty:
                print('\n---> No purchases have been made so far.')
            else:
                print(f'\nInvoice of purchases is as follows:\n\n{df}')

    @staticmethod
    def checking_inventory():
        try:
            df = pd.read_csv('products.csv')
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            is_empty = df.loc[df['inventory number'] == 0].empty
            if not is_empty:
                df1 = df.loc[df['inventory number'] == 0]
                df2 = df1.filter(['name', 'brand'])
                print(f'Note that the following products have zero inventory:\n\n{df2}')
                names = df2['name'].values
                for i in names:
                    logging.warning(f'The inventory of {i} was zero.')

    @staticmethod
    def unblocking(username):
        try:
            df = pd.read_csv('accounts.csv')
        except FileNotFoundError as e:
            print(e)
            logging.error(e)
        else:
            row_number = df.index[df['usr'] == username].tolist()
            df.loc[row_number[0], 'status'] = 1
            df.to_csv('accounts.csv', index=False)















