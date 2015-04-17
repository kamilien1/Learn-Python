# taken from https://courses.edx.org/courses/MITx/6.00.1x/3T2013/courseware/Week_2/Problem_Set_2/
# problem #3 https://courses.edx.org/courses/MITx/6.00.1x/3T2013/courseware/d5d822451677476fbfb0a0f9a14e0501/58b13e8f74a9407583d416d0be5ec907/


hi = balance
lo = 0
tmp_balance = balance

def balance_after_one_year(balance,annualInterestRate,payment):
    for _ in xrange(12):
        balance=(balance-payment) * (1+annualInterestRate/12.0)
    return balance

while True:
    payment = (hi + lo) / 2.0  
    tmp_balance= balance_after_one_year(balance,annualInterestRate,payment)
    if tmp_balance < -.01:
        hi = payment
    elif tmp_balance > .01:
        lo = payment
    else:
        break

print 'Lowest Payment:', round(payment, 2)