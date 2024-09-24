# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
# Simple Calculator to calculate Break-Even Point

def calculate_break_even():
    # Prompt the user to input fixed costs and convert the input to a float
    fixed_costs = float(input("Enter fixed costs: "))

    # Prompt the user to input variable cost per unit and convert to float
    variable_cost_per_unit = float(input("Enter variable cost per unit: "))

    # Prompt the user to input selling price per unit and convert to float
    selling_price_per_unit = float(input("Enter selling price per unit: "))

    # Calculate the break-even point (number of units to sell to cover all costs)
    break_even_point = fixed_costs / (selling_price_per_unit - variable_cost_per_unit)

    # Display the break-even point, formatted to 2 decimal places
    print(f"Break-Even Point: {break_even_point:.2f} units")

# Main function to run the program
def main():
    calculate_break_even()

# Call the main function to execute the program
if __name__ == "__main__":
    main()


