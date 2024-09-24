# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
# Simple Calculator to calculate Total Price after Tax

def calculate_total_price():
    # Prompt the user to input the product price and convert it to a float
    price = float(input("Enter product price: "))

    # Prompt the user to input the sales tax rate (e.g., input 0.07 for 7%)
    tax_rate = float(input("Enter sales tax rate (e.g., 0.07 for 7%): "))

    # Calculate the total price after tax: price + (price * tax_rate)
    total_price = price + (price * tax_rate)

    # Display the total price after tax, formatted to 2 decimal places
    print(f"Total price after tax: {total_price:.2f}")


# Main function to run the program
def main():
    calculate_total_price()

# Call the main function to execute the program
if __name__ == "__main__":
    main()

S