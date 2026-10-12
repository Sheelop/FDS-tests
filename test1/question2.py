#Write a program to calculate simple interest based on Principal, Rate and Time
p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time: "))
SI = (p*r*t)//100
print("Simple Interest = ",SI)