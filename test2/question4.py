# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.
cost_per_sqft = float(input("Enter the cost of painting per square foot: "))
length = float(input("Enter the length of the wall in feet: "))
width = float(input("Enter the width of the wall in feet: "))
area = 4 * (length * width)
total_cost = area * cost_per_sqft
print(f"Total cost of painting the interior of the building: {total_cost} Rs")