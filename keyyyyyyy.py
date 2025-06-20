# Define a function to calculate the due amount
def calculate_due_amount():
    # Get the total bill from the customer
    total_bill = float(input("Enter the total bill amount: ₹"))

    # Get the amount paid by the customer
    amount_paid = float(input("Enter the amount paid: ₹"))

    # Calculate the due amount
    due_amount = total_bill - amount_paid

    # Print the result
    if due_amount > 0:
        print("Customer still owes ₹", due_amount)
    elif due_amount == 0:
        print("Bill fully paid. No due amount.")
    else:
        print("Extra paid! Return ₹", -due_amount, "to customer.")

# Call the function to run the program
calculate_due_amount()
