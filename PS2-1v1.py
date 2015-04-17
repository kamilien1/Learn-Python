balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# pb = present balance, nb = next balance
pb = balance
totalPaid = 0
nb = 0

for i in range(0,12):
    print('Month: ' +str(i+1))
    print('Minimum monthly payment: ' + str(round(pb*monthlyPaymentRate,2)))
    totalPaid += round(pb*monthlyPaymentRate,2)    
    pb = round(pb*(1-monthlyPaymentRate),2)
    nb = round(pb*(1+annualInterestRate/12),2)
    pb = round(nb,2)
    print('Remaining balance: ' + str(nb))

print('Total paid: ' + str(totalPaid))
print('Remaining balance: ' + str(nb))