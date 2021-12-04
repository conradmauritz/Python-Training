# Calculate the gross pay based on the hours and rate provided by the user
# If the hours provided are more than 40 then the payment rate for the hours over 40
# will be 1.5 times more

hours_worked = float(input("Enter the amount of hours worked: "))
payment_rate = float(input("Enter the hourly payment rate: "))

standard_hours = 40

if hours_worked > standard_hours:
    overtime_hours = hours_worked - standard_hours
    gross_pay = round((standard_hours * payment_rate) + (overtime_hours * (payment_rate * 1.5)), 2)
else:
    gross_pay = round((standard_hours * payment_rate), 2)

print("The total payment amount is:", gross_pay)
