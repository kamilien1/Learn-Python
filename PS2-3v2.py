balance = 320000
annualInterestRate = 0.2
# Lowest Payment: 29157.0999983


# function that returns the balance after 12 months, monthly compout interest
def balance_after_one_year(balance,annualInterestRate,payment):
    for _ in xrange(12):
        balance=(balance-payment) * (1+annualInterestRate/12.00)
    return balance



# minPay is the min amount to pay, which would produce the largest leftover balance
# maxPay is the max amount to pay, which would produce the smallest leftover balance
# lowestPay is halfway between min and max pay

minPay = round(balance/12,2)
maxPay = round((balance * (1+annualInterestRate/12)**12)/12,2)
lowestPay = (minPay+maxPay)/2


# flag the answer as done
flag = True

while flag:
    
    endingBalance = balance_after_one_year(balance, annualInterestRate, lowestPay)
    

    # the ending balance is within 0.2 of 0
    if abs(round(endingBalance,2)) <= 0.2:
        print 'Found it'
        flag = False
    
    # the ending balance is too low, therefore the guess lowest pay was too high and we must adjust our guess downward
    elif endingBalance < 0.2:
        maxPay = lowestPay
        lowestPay = (minPay+maxPay)/2

    # the ending balance is too high, therefore the guess lowest pay was too low and we must adjust our guess upward
    elif endingBalance > 0.2:
        minPay = lowestPay
        lowestPay = (minPay+maxPay)/2
        
    
print 'Lowest Payment: ', round(lowestPay,2)