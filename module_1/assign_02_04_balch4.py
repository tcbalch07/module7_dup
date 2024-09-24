# Tucker Balch
# CBIS 6391 A2
# Assignment 1.1
# 8/28/2024
#Simple Calculator to calculate Net Income

def calculate_net_income():
    # Collecting inputs from the user
    net_sales = float(input("Enter Net Sales: "))
    cost_of_goods_sold = float(input("Enter Cost of Goods Sold: "))
    operating_expenses = float(input("Enter Operating Expenses: "))
    depreciation_amortization = float(input("Enter Depreciation and Amortization: "))
    interest_expenses = float(input("Enter Interest Expenses: "))
    tax_rate = float(input("Enter Tax Rate (as a decimal, e.g., 0.25 for 25%): "))

    # Calculating EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization)
    ebitda = net_sales - cost_of_goods_sold - operating_expenses

    # Calculating Operating Income (EBIT)
    ebit = ebitda - depreciation_amortization

    # Calculating Earnings Before Tax (EBT)
    ebt = ebit - interest_expenses

    # Calculating Taxes based on EBT
    taxes = ebt * tax_rate

    # Calculating Net Income (NI)
    net_income = ebt - taxes

    # Displaying the result
    print(f"Net Income (NI): {net_income:.2f}")

# Running the function
calculate_net_income()
