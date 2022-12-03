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

    def __init__(self):
        self.accounts = []

    def __str__(self):
        """ String representation of the bank """
        return "Bank with %d accounts" % len(self.accounts)
    
    def __repr__(self):
        """ Representation of the bank """
        return self.__str__()


    def __findAccount(self, name):
        """ Find account associated to name
            @name: str(name) of the account
            @return Account() if found, None if not
        """
        return next((x for x in self.accounts if x.name == name), None)
    
    def __accountHasFunds(self, account_name, amount):
        """ Check if account has funds
            @account_name: str(name) of the account
            @amount: float(amount) amount to transfer
            @return True if has fund, False if not
        """
        account = self.__findAccount(account_name)
        if account == None: return False
        return account.value >= amount

    def __checkAccountCorruption(self, account_name):
        """ Check if account is valid
            @account_name: str(name) of the account
            @return True if valid, False if not
        """
        account = self.__findAccount(account_name)
        if account == None: return False
        if len(account.__dict__) % 2 == 0: return False
        for i in account.__dict__:  # type: ignore
            if i.startswith('b'): return False
        if not hasattr(account, 'zip') and not hasattr(account, 'addr'): return False
        for i in ['name', 'value', 'id']:
            if not hasattr(account, i): return False
        if not isinstance(getattr(account, 'name'), str): return False
        if not isinstance(getattr(account, 'id'), int): return False
        if not isinstance(getattr(account, 'value'), (int, float)): return False
        return True

    def __transferPriorValidityCheck(self, from_account, to_account, amount):
        """ Perform a prior check and validates the accounts and the amount
            @from_account: str(name) of the first account
            @to_account: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not self.__checkAccountCorruption(from_account): return False
        if not self.__checkAccountCorruption(to_account): return False
        if amount < 0 or not self.__accountHasFunds(from_account, amount): return False
        return True

    def __addAccountValidityCheck(self, new_account):
        """ Perform a prior check and validates the account
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account): return False
        if self.__findAccount(new_account.name) != None: return False
        return True

    def __checkAccountBeforeFix(self, account_name):
        """ Check if account is valid before fixing it
            @account_name: str(name) of the account
            @return True if valid, False if not
        """
        if not isinstance(account_name, str): return False
        account = self.__findAccount(account_name)
        if account == None: return False
        return True


    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not self.__addAccountValidityCheck(new_account): return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not self.__transferPriorValidityCheck(origin, dest, amount): return False
        origin, dest = self.__findAccount(origin), self.__findAccount(dest)
        if origin == None or dest == None: return False
        origin.transfer(-amount)
        dest.transfer(amount)
        return True

    def fix_account(self, name):
        """ Fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not self.__checkAccountBeforeFix(name): return False
        if self.__checkAccountCorruption(name): return True
        account = self.__findAccount(name)
        for i in list(account.__dict__):  # type: ignore
            if i.startswith('b'): delattr(account, i)
        if not hasattr(account, 'addr'): setattr(account, 'addr', 'unknown')
        if not hasattr(account, 'zip'): setattr(account, 'zip', 0)
        if not isinstance(getattr(account, 'name'), str): setattr(account, 'name', name)
        if not isinstance(getattr(account, 'id'), int): setattr(account, 'id', Account.ID_COUNT)
        if not isinstance(getattr(account, 'value'), (int, float)): setattr(account, 'value', 0)
        # Account.ID_COUNT += 1  # type: ignore
        return True
