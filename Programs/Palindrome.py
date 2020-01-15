#taking user input
num = int(input("Enter a number:"))

temp=num
rev= 0


#getting the reverse of the input number
while(num>0):
    dig = num%10
    rev = rev*10 + dig
    num = num//10


#displaying the result
if(temp == rev):
    print(temp," is a Palindrome number!")

else:
    print(temp, " is not a Palindrome number!")