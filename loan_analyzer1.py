# coding: utf-8

#  imports csv module to enable us to output to a csv file.

#  imports the Path module from the pathlib library to enable us to set the output file path.

import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan1_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

#  creating list_len object to hold the value of using the 'len' function to count length of our list 'loan_cost' 

#  using formatting to selectively insert 'list_len' into our print statement  
  
list1_len = len (loan1_costs)
print(f'There are {list1_len} loans in total.' )

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

#  creating cost object to hold the value of using the 'sum' function to sum the total of all loan 'loan_cost' 

#  using formatting to selectively insert 'c' into our print statement and ${<float value>:.2f} for presentation
 
cost = sum (loan1_costs)
print(f"The total value of the all loans ${cost:.2f}.")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

#  creating ave_loan_price object to hold the value of averaging cost over list length.

#  using formatting to selectively insert 'ave_loan_price' into our print statement and ${<float value>:.2f} for presentation

ave_loan_price1 = cost / list1_len
print(f"The average loan amount is ${ave_loan_price1:.2f}.")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

#  using get() on the dictionary to extract the future_value and remaining_months and sotred in similarly names variables

#  instead of printing direct, I stored the value to be able to format my string to meet professors expected outcome. 

future_value = (loan.get("future_value"))
remaining_months = (loan.get("remaining_months"))


#  using formatting to selectively insert 'future_value' into our print statement and ${<float value>:.2f} for presentation

#  using formatting to selectively insert 'remaining_months' into our print statement  

print(f"The future value of the loan is ${future_value:.2f}.")
print(f"There are {remaining_months:} months remaining on the loan.")



# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

discount_rate = 0.20

def calculate_present_value(loan, annual_discount_rate):
    present_value = loan["future_value"] /(1 + annual_discount_rate / 12)**loan["remaining_months"]
    return present_value

present_value = calculate_present_value(loan, discount_rate)


print(f"The present value of the loan is: {present_value}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if present_value > ave_loan_price1:
    print("Our model is evaluating this loan to be worth cost price, with a posible consideable upside ")
elif present_value < ave_loan_price1:
    print("This loan doesnt not meant the return desire")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

present_value = calculate_present_value(new_loan, discount_rate)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

inexpensive_loans = []


# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

for loan in loans:
    if(loan["loan_price"] <= 500):
        inexpensive_loans.append(loan)
 


# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

print(inexpensive_loans)        

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

with open(output_path, "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for loan in inexpensive_loans:
            writer.writerow(loan)
