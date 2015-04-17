#balance = 4111
#annualInterestRate = 0.15

balance = 320000
annualInterestRate = 0.2

payment = 0
def balance_after_one_year(balance,annualInterestRate,payment):
    for _ in xrange(12):
        balance=(balance-payment) * (1+annualInterestRate/12.0)
    #print 'balance is ', balance 
    return balance

while balance_after_one_year(balance, annualInterestRate, payment) > 0:
    payment += 0.01
    #print 'payment is ', payment

print 'Lowest Payment:', payment