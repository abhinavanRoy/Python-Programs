#Take input from user
num1 = int(input("Enter the 1st number:"))  
num2 = int(input("Enter the 2nd number:"))
num3 = int(input("Enter the 3rd number:"))


#computing  the largest number
if(num1 > num2) and (num1 > num3):

    largest  = num1
elif(num2 > num1) and (num2 > num3):

    largest = num2
         
else:
    largest = num3



#display the largest number
print("The largest number among ",num1,",",num2,",",num3," is ", largest)

