#     Test Case 1:
#	      balance = 3329
#	      annualInterestRate = 0.2
#
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 310

#balance = 3329 
# lowest payment = 310

#annualInterestRate = 0.2

#balance = 4773
# lowest payment = 440

#balance = 3926
# lowest payment = 360

# 0.15 ir test



balance = 320000
annualInterestRate = 0.2
# Lowest Payment: 29157.0999983


# ub - unpaid balance
# uub - updated unpaid balance
# mp = monthly payment, incremented by 10
# flag - set to true until balance is <= 0 after 12 months of payments


ub = balance
flag = True
minPay = round(balance/12,2)
maxPay = round((balance * (1+annualInterestRate/12)**12)/12,2)
# start in the middle
guessPay = (minPay+maxPay)/2

def balance_after_one_year(balance1,annualInterestRate,payment):
    for _ in xrange(12):
        balance1=(balance1-payment) * (1+annualInterestRate/12.00)
    return balance1
    
leastNeg = balance_after_one_year(balance, annualInterestRate,maxPay)
leastPos = balance_after_one_year(balance, annualInterestRate, minPay)

while flag:
    
    ub = balance_after_one_year(balance, annualInterestRate, guessPay)
   # print('test ub is: ' + str(ub)+ ' and guessPay is ' + str(guessPay))
    
    # if ub is lower than 0 and still lower than the least negative
    if ub < 0 and ub > leastNeg:
        leastNeg = ub
        minPay = guessPay
        guessPay = (minPay+maxPay)/2.00
        print 'in 1st if'
        
    # if ub  is higher than 0 and still less than the least positive unpaid balance 
    elif ub > 0 and ub < leastPos:
        leastPos = ub
        maxPay = guessPay
        guessPay = (minPay+maxPay)/2.00
        print 'in 2nd if'
                
    # when under 0.01 we can exit
    elif (maxPay-guessPay <= 0.01) or (guessPay-minPay <= 0.01):
        print('Found an answer')
        flag = False
    
    # in case I messed up
    else:
        print 'maxPay-guessPay = ', maxPay-guessPay
        print 'minPay-guessPay = ', minPay-guessPay
        print 'maxPay= ', maxPay, 'minPay= ',minPay, 'guessPay= ',guessPay
        print 'ub= ', ub
        print 'leastNeg= ', leastNeg
        print 'leastPos= ', leastPos
        flag = False
    
    

print('Lowest Payment: ' + str(guessPay))