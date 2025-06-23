class BankAccount:
    def __init__(self):
        self.account_number = None
        self.account_type = None
        self.account_owner_name = None
        self.account_owner_ssn = None
        self.balance = 0.0

    def set_account_number(self, number):
        self.account_number = number

    def set_account_type(self, acc_type):
        self.account_type = acc_type

    def set_account_owner_name(self, name):
        self.account_owner_name = name

    def set_account_owner_ssn(self, ssn):
        self.account_owner_ssn = ssn

    def set_balance(self, amount):
        self.balance = amount


def create_bank_account(account_number, account_type, account_name, account_ssn, balance):
    account = BankAccount()
    account.set_account_number(account_number)
    account.set_account_type(account_type)
    account.set_account_owner_name(account_name)
    account.set_account_owner_ssn(account_ssn)
    account.set_balance(balance)

    return account
