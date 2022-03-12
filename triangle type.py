#WAP that accepts three side of triangle and check the type of triangle.
a=int(input("Enter the side:"))
b=int(input("Enter the side:"))
c=int(input("Enter the side:"))
if a==b or b==c or c==a: 
    print("The triangle is isosceles triangle.")
if a==b and b==c:
    print("The triangle is equilateral triangle.")
else:
    print("The triangle is scalene triangle.")
input()    
