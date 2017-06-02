"""
Day 2: Operators

Given the meal price (base cost of a meal),
tip percent (the percentage of the meal price
being added as tip), and tax percent (the
percentage of the meal price being added as tax)
for a meal, find and print the meal's total cost.
"""

def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(raw_input())
    # tip percentage
    tip_percent = float(raw_input())
    # tax percentage
    tax_percent = float(raw_input())

    # Write your calculation code here
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)

    # cast the result of the rounding operation to an int and save it as total_cost
    total_cost = int(round(meal_cost + tip + tax))

    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
