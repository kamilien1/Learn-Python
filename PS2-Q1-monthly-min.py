"""
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

Month - 1-12
"""

Month = 1
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total_paid = 0

monthly_interest_rate = annualInterestRate/12

for Month in range(1,13):
    
   
    #update new min to pay for the month
    min_m_payment = balance*monthlyPaymentRate
    #update the balance in 2 steps, first, pay your min payment
    new_balance = balance - min_m_payment
    # second, add interest
    new_balance = new_balance*(1+monthly_interest_rate)
    # third, the balance is now updated and repeate the loop
    balance = new_balance
    total_paid += min_m_payment



# round(float,2) rounds the float to 2 decimal points!

    print 'Month: ', Month
    print 'Minimum monthly payment: ', round(min_m_payment,2)
    print 'Remaning balance: ', round(new_balance,2)

print 'Total paid: ', round(total_paid,2)
print 'Remaining balance: ', round(new_balance,2)