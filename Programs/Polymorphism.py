
#function 
def poly(x,y,z = 0):
    return x + y + z


# taking interger input from user
x = int(input("Enter a number in integer:"))
y = int(input("Enter another number in integer:"))

#funcion called
print(poly(x,y))


#taking float input from user 
x = float(input("Enter a number in float:"))
y = float(input("Enter another number in float:"))
z = float(input("Enter another number in float:"))

# function called
print(poly(x,y,z))