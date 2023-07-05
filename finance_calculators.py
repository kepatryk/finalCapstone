import math

# Outputs instructions for the user to choose between investement or bond calculations
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.\n")

calculation_type = input("Enter either 'investement' or 'bond' from the menu above to proceed: ").lower()


# The while loops allows us to run the programme and get back to the original even if the users enters an invalid answer
while (calculation_type != "investement") and (calculation_type != "bond"):
    print("You have entered an invalid answer.\n")
    calculation_type = input("Please enter either 'investement' or 'bond': \n").lower()
    
# The questions below will be asked if the user enters "investement"
if calculation_type == "investement":  
    print("\nOkay, let's calculate the amount of interest you'll earn on your investement. Please answer the questions below.\n")

    deposit_amount = float(input("How much money are you depositing? "))
    interest_rate = float(input("What's your current interest rate in % ? ")) 
    years_of_investement = float(input("How many years are you planning on investing? "))
    interest = input("Would you like the calculation for a 'simple' or 'compound' interest? ").lower()

    # This while loop is here to ensure the programme doesn't stop if the user enters an invalid answer
    while (interest != "simple") and (interest != "compound"):
        print("You have entered an invalid answer.")
        interest = input("Please choose between a 'simple' or 'compound' interest: ").lower()

    # The following code calculates the total amount when simple interest is applied. The total amount is rounded to the 2nd decimal number
    if interest == "simple":
        total_amount = round(deposit_amount * (1 + (interest_rate / 100) * years_of_investement), 2)
        print(f"Your total amount after {years_of_investement} years of investement when a simple interest is applied is £{total_amount}.")

    # The following code calculates the total amount when compound interest is applied
    else:
        total_amount = round(deposit_amount * math.pow((1 + (interest_rate / 100)), years_of_investement), 2)
        print(f"Your total amount after {years_of_investement} years of investement when a compound interest is applied is £{total_amount}.")

# The questions below will be asked if the user enters "bond" instead of "investement"
else :
    print("Okay, let's calculate the amount you'll have to pay each month on your loan. Please answer the questions below.\n")

    house_value = float(input("What is the current value of the house in £ ? "))
    interest_rate = float(input("What's your current interest rate in % ? "))
    months_to_repay = float(input("How long is it going to take you to repay the bond? Please provide your answer in months: "))

    # The following code calculates how much mone the user will have to repay each month. The value is rounded to the 2nd decimal place.
    repayment = round((((interest_rate / 100) /12) * house_value) / (1 - (1 + ((interest_rate / 100) /12)) ** (- months_to_repay)), 2)
    print(f"The amount of money you will have to repay each month is £{repayment}.")



    

    

