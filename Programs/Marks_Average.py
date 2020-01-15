total =0

#calculating total marks
for i in range(1,6):
    print("Enter mark of " , i, "subject:")
    mark= int(input())
    total +=mark 

#finding average
avg = total / 5

#displaying the results
print("The total is:", total)
print("The average is:", avg)
