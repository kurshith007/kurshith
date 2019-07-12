numb1 = float(input("Enter first number: "))
numb2 = float(input("Enter second number: "))
numb3 = float(input("Enter third number: "))
 
if (numb1 > numb2) and (numb1 > numb3):
   largest = numb1
elif (numb2 > numb1) and (numb2 > numb3):
   largest = numb2
else:
   largest = numb3
 
print("The largest number is",largest)
