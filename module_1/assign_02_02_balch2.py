# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
# Simple Calculator to calculate Loan Payment

# Simple Calculator to calculate Loan Payment

def calculate_loan_payment():
    # Prompt the user to input the loan amount and convert it to a float
    loan_amount = float(input("Enter loan amount: "))

    # Prompt the user to input the annual interest rate and convert it to a float
    annual_rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))

    # Prompt the user to input the loan term in years and convert it to an integer
    years = int(input("Enter loan term in years: "))

    # Calculate the monthly interest rate by dividing the annual rate by 12
    monthly_rate = annual_rate / 12

    # Calculate the total number of months for the loan term
    months = years * 12

    # Use the loan payment formula to calculate the monthly payment
    # P = loan amount, r = monthly rate, n = total number of months
    payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

    # Display the calculated monthly payment, formatted to 2 decimal places
    print(f"Monthly Payment: {payment:.2f}")

# Main function to run the program
def main():
    calculate_loan_payment()

# Call the main function to execute the program
if __name__ == "__main__":
    main()


