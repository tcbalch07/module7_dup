# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
# Simple Calculator to calculate Break-Even Point

def calculate_break_even():
    fixed_costs = float(input("Enter fixed costs: "))
    variable_cost_per_unit = float(input("Enter variable cost per unit: "))
    selling_price_per_unit = float(input("Enter selling price per unit: "))

    break_even_point = fixed_costs / (selling_price_per_unit - variable_cost_per_unit)

    print(f"Break-Even Point: {break_even_point:.2f} units")


calculate_break_even()
