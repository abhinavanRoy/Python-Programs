
# class created
class calculate:
     
    # Constructor
    def __init__(self):
        print("Construtor called!")
    
    # Function to find square
    def square(self,x):
        res = x ** 2
        print("The square of",x,"is",res)
    
    # functon to find cube
    def cube(self,x):
        res = x ** 3
        print("The cube of",x,"is",res)

    # Destructor
    def __del__(self):
        print("Destructor called!")

        

# class instance created
obj = calculate()

# taking input from user
x  = int(input("Enter a number:"))

# function calls
obj.square(x)
obj.cube(x)
