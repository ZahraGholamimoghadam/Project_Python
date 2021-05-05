import csv
import pandas as pd


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
        with open("invoices.csv") as file:
            df = pd.read_csv(file)
            if df.empty:
                print('\n---> No purchases have been made so far.')
            else:
                print(f'\nInvoice of purchases is as follows:\n\n{df}')

    def checking_inventory():
        df = pd.read_csv('products.csv')
        is_empty = df.loc[df['inventory number'] == 0].empty
        if is_empty == False:
            print(f'Note that the following products have zero inventory:\n\n'
                  f'{df.loc[df["inventory number"] == 0]}')












