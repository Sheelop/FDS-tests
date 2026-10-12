# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field
circle = 3.14 * 20
rectangle = 2 * (50 + 40)
total_length = circle + rectangle
total_cost = total_length * 35 * 5
print(f"Total cost of fencing the field: {total_cost} Rs")