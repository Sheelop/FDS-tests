# #Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)
area = int(input("Enter area of painting the wall: "))
cost_external = int(input("Enter cost of external wall: "))
cost_internal = int(input("Enter cost of internal wall: "))
total_cost = ((area*cost_external) + (cost_internal*area))*4 
print("Total cost = ",total_cost)