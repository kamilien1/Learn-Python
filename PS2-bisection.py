balance = 999999
annualInterestRate = 0.18


mir = annualInterestRate/12


lb = balance / 12.0
ub = (balance * (1+mir)**12)/12.0
fixed_pay = (lb+ub)/2

mub = balance - fixed_pay
mub = mub*(1+mir)

lowest_found = False

while lowest_found == False:
    
    test_balance = balance * 1.00
    
    for i in range(1,13):
        mub = test_balance - fixed_pay
        mub = mub*(1+mir)
        test_balance = mub
        
    if abs(test_balance)-0.01 > 0:
        if test_balance > 0:
            lb = fixed_pay    
            fixed_pay = (ub + lb)/2
        else:
            ub = fixed_pay
            fixed_pay = (ub+lb)/2
    else:
        lowest_found = True
        break

print 'Lowest Payment: ', round(fixed_pay,2)