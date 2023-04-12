
#Cash Dispenser Application

acc_01 = {
    'Name': 'Abraham Washington',
    'AccountNumber':'159487',
    'Balance':1500,
    'Credit':2500,
}

acc_02 = {
    'Name': 'George Obama',
    'AccountNumber':'362951',
    'Balance':1200,
    'Credit':2800,
}

def withdraw_money (account,amount):
    print(f"Hello {account['Name']}")

    if (account['Balance']>=amount):
        print('You can withdraw your money without using Credit')
    else:
     total=account['Balance']+account['Credit']
     if(total>=amount):
        CreditUsing=input('Do you want to use Credit (Y/N)')
        if CreditUsing=='Y':
           print('You can withdraw your money')
        else:
           print('You cant withdraw your money')
     else:
        print('Sorry, you have insufficient balance')  

        

    withdraw_money(acc_01,1750)