# in the_bank.py
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'): self.value = 0
        if self.value < 0: raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str): raise AttributeError("Attribute name must be a str object.")
        
    def transfer(self, amount):
        self.value += amount


class Bank:
    """The bank"""

    def __checkAccountExistence(self, account):
        for i in self.accounts:
            if i.name == account: return True
        return False

    def __checkAccountCorruption(self, account):
        """ Check if account is corrupted
            @account: str(name) of the account
            @return True if corrupted, False if not
        """
        attributes_list = ['name', 'value', 'id']
        for i in self.accounts:
            if getattr(i, 'name') == account:
                if len(i.__dict__) % 2 == 0: return True
                for j in i.__dict__:
                    if j.startswith('b'): return True
                if not hasattr(i, 'zip') and not hasattr(i, 'addr'): return True
                for k in attributes_list:
                    if not hasattr(i, k): return True
                if not isinstance(getattr(i, 'name'), str): return True
                if not isinstance(getattr(i, 'id'), int): return True
                if not isinstance(getattr(i, 'value'), (int, float)): return True
        return False

    def __checkAccountsValidity(self, origin: str, dest: str, amount):
        """ Check if accounts are valid
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if valid, throws Exception if not
        """
        if not isinstance(amount, (float, int)): raise AttributeError('amount must be a float or an int')
        if amount < 0: raise AttributeError('amount cannot be negative')
        if not self.__checkAccountExistence(origin): raise AttributeError('origin account does not exist')
        if not self.__checkAccountExistence(dest): raise AttributeError('destination account does not exist')
        return True


    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account): raise AttributeError('new_account is not an instance of Account')
        if self.__checkAccountExistence(new_account.name): raise AttributeError('new_account already exists')
        self.accounts.append(new_account)
        

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if self.__checkAccountsValidity(origin, dest, amount): return False
        origin.transfer(-amount)
        dest.transfer(amount)
        return True
        

    def fix_account(self, name):
        """ Fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str): return False
        for i in self.accounts:
            if i.name == name:
                if self.__checkAccountCorruption(name):
                    if len(i.__dict__) % 2 == 0: i.__dict__.popitem()
                    for j in i.__dict__:
                        if j.startswith('b'): i.__dict__.pop(j)
                    if not hasattr(i, 'zip') and not hasattr(i, 'addr'): i.__dict__.pop('addr')
                    for k in ['name', 'value', 'id']:
                        if not hasattr(i, k): setattr(i, k, None)
                    if not isinstance(getattr(i, 'name'), str): setattr(i, 'name', None)
                    if not isinstance(getattr(i, 'id'), int): setattr(i, 'id', None)
                    if not isinstance(getattr(i, 'value'), (int, float)): setattr(i, 'value', None)
                    return True
        return False
