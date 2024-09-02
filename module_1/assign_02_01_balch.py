# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
# Simple Calculator to calculate Total Price after Tax

def calculate_total_price():
    price = float(input("Enter product price: "))
    tax_rate = float(input("Enter sales tax rate (e.g., 0.07 for 7%): "))
    total_price = price + (price * tax_rate)
    print(f"Total price after tax: {total_price:.2f}")

calculate_total_price()
