#Write a program to find area and perimeter of following figure 
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
r = int(input("Enter radius: "))
area = (l*b) + ((3.14*r**2)//2)
perimeter = 2*(l+b) + 3.14*r
print("Area of the figure is: ", area)
print("Perimeter of figure is: ",perimeter)
