# Calculate the gross pay based on the hours and rate provided by the user

hours = float(input("Enter the amount of hours worked: "))
rate = float(input("Enter the hourly payment rate: "))
gross_pay = round((hours * rate), 2)
print("The total payment amount is:", gross_pay)
