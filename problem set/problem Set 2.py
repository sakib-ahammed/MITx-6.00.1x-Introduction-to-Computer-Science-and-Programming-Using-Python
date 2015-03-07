### problem 1

monthlyInterestRate = annualInterestRate / 12
annualPayment = 0.0
for month in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    updatedBalanceEachMonth = (balance - minimumMonthlyPayment) * (1 + monthlyInterestRate)
    annualPayment += minimumMonthlyPayment
    print("Month: {0}".format(month))
    print("Minimum monthly payment: {0:.2f}".format(minimumMonthlyPayment))
    print("Remaining balance: {0:.2f}".format(updatedBalanceEachMonth))
    balance = updatedBalanceEachMonth
print("Total paid: {0:.2f}".format(annualPayment))
print("Remaining balance: {0:.2f}".format(balance))


### problem 2

payment_base = 0
balance_new = balance

while balance_new > 0:
    balance_new = balance
    payment_base += 10
    if payment_base > (balance_new * annualInterestRate / 12):
        for i in range(12):
            balance_new -= payment_base
            balance_new += (balance_new * annualInterestRate / 12)

print 'Lowest Payment: %s' % (payment_base)


### problem 3

def pay_off_debt_in_a_year(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    updatedBalanceEachMonth = balance
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
    minimumMonthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2.0
    
    while abs(monthlyPaymentUpperBound - monthlyPaymentLowerBound) > 0.000001:
        minimumMonthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2.0
        updatedBalanceEachMonth = balance
        
        for i in range(12):
            updatedBalanceEachMonth = (updatedBalanceEachMonth - minimumMonthlyPayment) * (1 + monthlyInterestRate)
            
            
        if updatedBalanceEachMonth >= 0.0:
            monthlyPaymentLowerBound = minimumMonthlyPayment
        else:
            monthlyPaymentUpperBound = minimumMonthlyPayment
        

    print("Lowest Payment: {0:.2f}".format(minimumMonthlyPayment))

pay_off_debt_in_a_year(balance, annualInterestRate)
