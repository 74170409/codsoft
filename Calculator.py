first = input("Enter the first number:")
second = input("Enter the second number:")
first = int(first)
second = int(second)

print("---- Press key for operator (+,_,/,%,*) ----")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")