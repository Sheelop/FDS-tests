# Write a function to which we pass a parameter and
# print the factors of a given number
# For Eg: Factors of 12 : 1,2,3,4,6,12
def print_factors(num):
    print("Factors of", num, ":")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=", ")
    print()  
num = int(input("Enter a number: "))
print_factors(num)