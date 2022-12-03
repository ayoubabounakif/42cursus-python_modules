from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    ))

    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')






# if __name__ == "__main__":
#     bank = Bank()
#     bank.add(Account(
#         'Smith Jane',
#         zip='911-745',
#         value=1000.0,
#         ref='1044618427ff2782f0bbece0abd05f31'
#     ))
#     bank.add(Account(
#         'William John',
#         zip='100-064',
#         value=6460.0,
#         ref='58ba2b9954cd278eda8a84147ca73c87',
#         info=None
#     ))

#     if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
#         print('Failed')

#         bank.fix_account('William John')
#         bank.fix_account('Smith Jane')

#     if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
#         print('Failed')
#     else:
#         print('Success')







# if __name__ == "__main__":
#     bank = Bank()
#     acc_valid_1 = Account('Sherlock Holmes',
#                           zip='NW1 6XE',
#                           addr='221B Baker street'
#                           value=1000.0)
#     acc_valid_2 = Account('James Watson',
#                           zip='NW1 6XE',
#                           addr='221B Baker street',
#                           value=25000.0,
#                           info=None)
    
#     acc_invalid_4 = Account("Douglass",
#                             zip='42',
#                             addr='boulevard bessieres',
#                             value=42)
#     acc_invalid_1 = Account("Adam",
#                             value=42,
#                             zip='0',
#                             addr='Somewhere')
#     acc_invalid_2 = Account("Bender Bending RodrÃ­guez",
#                             zip='1',
#                             addr='Mexico',
#                             value=42)
#     acc_invalid_3 = Account("Charlotte",
#                             zip='2',
#                             addr='Somewhere in the Milky Way',
#                             value=42)
#     acc_invalid_5 = Account("Edouard",
#                             zip='3',
#                             addr='France',
#                             value=42)
    
#     bank.add(acc_valid_1)
#     bank.add()

#     #if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
#     #    print('Failed')
#     #    bank.fix_account('William John')
#     #    bank.fix_account('Smith Jane')
#     ## ...
#     #if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
#     #    print('Failed')
#     #else:
#     #    print('Success')