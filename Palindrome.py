# Input from user

num = int(input("Enter your Number:"))

# Storage orighnal number for comparision

temp = num

reversenum = 0

#Reverse the Number

while temp > 0:

    digit = temp%10

    reversenum = (reversenum*10)+digit

    temp=temp//10

#Check if orginal and reverse num are same

if num == reversenum:

    print(f"{num} is a palindrome")

else:

    print(f"{num} not a palindrome")