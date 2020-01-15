#setting the upper and lower limit
lower = 1
upper = 50


#computing prime numbers
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i)==0:
                break
        
        else:
            print(num)    #displaying the numbers
                




