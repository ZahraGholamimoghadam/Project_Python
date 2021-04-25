
class Admin:
    def __init__(self, username, password):
        """
        :param username: username of customer
        :param password: password of customer
        """
        self.username = username
        self.password = password.encode()

    @staticmethod
    def create_product():
        return 'Admin defines barcode, price, brand, name and inventory number for every product. ' \
               'He does this work with saving these properties in a file.'

    @staticmethod
    def show_invoices():
        return 'Previous purchase invoice is displayed to admin.'