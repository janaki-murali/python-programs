from bank import Bank,SavingsAccount
from savings import RestrictedSavingsAccount

print('Create a restricted account')
racc = RestrictedSavingsAccount('Deepak','10000',1000)
print(racc)
racc.deposit(1000)
print('Withdrawals')
for i in range(4):
    print(racc.withdraw(10))

#saving a new bank and reading it
newbank = Bank()
newbank.add(SavingsAccount('Naveen','10001',2000))
newbank.add(SavingsAccount('Rishi','10002',21000))
newbank.add(SavingsAccount('Leena','10003',4000))
newbank.add(SavingsAccount('Mini','10004',5000))

#print(newbank)
newbank.save('newbank.dat')

nb = Bank('newbank.dat')
print('Loaded from pickle file')
print(nb)
