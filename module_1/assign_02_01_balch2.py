# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
# Simple Calculator to calculate Loan Payment

def calculate_loan_payment():
    loan_amount = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
    years = int(input("Enter loan term in years: "))

    monthly_rate = annual_rate / 12
    months = years * 12

    payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

    print(f"Monthly Payment: {payment:.2f}")


calculate_loan_payment()
