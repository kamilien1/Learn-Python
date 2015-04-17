balance = 4773
annualInterestRate = 0.2

fixed_pay = 0
mir = annualInterestRate/12

mub = balance - fixed_pay
mub = mub*(1+mir)

lowest_found = False

while lowest_found == False:
    
    test_balance = balance
    
    for i in range(1,13):
        mub = test_balance - fixed_pay
        mub = mub*(1+mir)
        test_balance = mub
        
    if test_balance > 0:
        fixed_pay += 10
    else:
        lowest_found = True
        break

print 'Lowest Payment: ', fixed_pay