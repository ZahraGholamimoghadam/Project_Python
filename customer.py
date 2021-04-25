import csv
import hashlib


class Customer:
    def __init__(self, username, password):
        """
        :param username: username of customer
        :param password: password of customer
        """
        self.username = username
        self.password = password.encode()

    def register(self):
        with open('accounts.csv', 'a') as file_accounts:
            writer_accounts = csv.DictWriter(file_accounts, fieldnames=['usr', 'pass'])
            writer_accounts.writerow({'usr': self.username, 'pass': hashlib.sha256(self.password).hexdigest()})

    @staticmethod
    def login():
        person = False
        with open('accounts.csv') as file_accounts:
            existing_rows = [row for row in csv.reader(file_accounts)]
        for i in range(3):
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if [username, hashlib.sha256(password.encode()).hexdigest()] in existing_rows:
                print('\n-->Your login was successful.')
                person = Customer(username, password) # Creates an instance
                break
        else:
            print('\n--> Your account was locked!')

        return person

    @staticmethod
    def show_products():
        return 'A list of all products is showed for customer.'

    @staticmethod
    def shopping():
        return 'Client selects some products.\n' \
               'The final purchase price is calculate and displayed.\n' \
               "An invoice is create based on the customer's purchase and saves in file.\n"\
               'At the final Inventory of purchased product is updated in file.' \



