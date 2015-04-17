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

balance = 4111
annualInterestRate = 0.15

# ub - unpaid balance
# uub - updated unpaid balance
# mp = monthly payment, incremented by 10
# flag - set to true until balance is <= 0 after 12 months of payments

mp = 10
ub = balance
flag = True

while flag:
    
    for i in range(1,13):
        
        ub = (ub-mp)*(1+annualInterestRate/12.0)
    
    print('test ub is: ' + str(ub)+ ' and mp is ' + str(mp))
    if ub <= 0:
        flag = False
    else:
        ub = balance
        mp+=10

print('Lowest Payment: ' + str(mp))