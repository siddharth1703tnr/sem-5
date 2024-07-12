# assign-1 Program-2
# 2. Write Program for simple interest. Simple Interest = (P x T x R)/100

principal_amount = float(input("Enter Principal amount Of Lone(IN INR Only):-"))
rate_of_interest = float(input("Enter Rate of interest (in %):- "))
number_of_years = float(input("Enter Number of years:- "))

interest = (principal_amount*rate_of_interest*number_of_years)/100

print("The  simple interest IS:- ")
print(interest)

# OUTPUT ===>
# Enter Principal amount Of Lone(IN INR Only):-10000
# Enter Rate of interest (in %):- 5
# Enter Number of years:- 2
# The  simple interest IS:- 
#1000.0

# === Code Execution Successful ===
