x = int(input("Insert first number: "))
y = int(input("Insert second number: "))
z = int(input("Insert third number: "))

print("The maximum number is : ", end="")
if y<= x >=z:
    print(x)
elif x <= y >=z:
    print(y)
elif x<= z >= y:
    print(z)

#or next logic
if (x>y and x>z):
    print("x is the greatest")
elif (y>z):
    print("y is the greatest")
else:
    print("z is the greatest")