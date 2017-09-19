#Loan Calculator
#Accept the cost of loan amount from user
loan_amt = input("Enter the loan amount you want to borrow: ")

#Accept the interest rate from user
intr_rate = input("Enter the interest rate would like to take the loan: ")

#Accept the cost of number of years from user
num_pay = input("Enter the number of years to repay the loan: ")

#Converts the user entered values to respective datatypes
loan_amt = float(loan_amt)
intr_rate = float(intr_rate)

#Multiply 12 to number of years to get the number of payments because we are calculating for each month
num_pay = int(num_pay)
num_pay = num_pay * 12

#After accepting the user inputs
#calculate the monhtly payments for the above inputs and the calculation is divided into two lines using slash(\)
month_pay = loan_amt * intr_rate * (1 + intr_rate) * num_pay \
    / ((1 + intr_rate) * num_pay - 1)

#print the monthly payments 
print("The monthly payments for the is: %.2f " % month_pay)

#Printing the monthly payments in .format
print("The monthly payments for the is: {0:.2f} " .format(month_pay))
