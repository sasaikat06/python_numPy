def sum(x,y):
    return x+y

def subtract(x,y):
    if x>y:
      return x-y
    else:
        return y-x

def product(x,y):
    return x*y

def division(x,y):
    if y != 0:
      return x/y
    else:
       return("0 is mysterious, Bro!")
    
result = 0

while True:
   print("Simple calculator")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   print("5. I'm Out!")

   choice = input("Enter a number: [1,5]")

   if choice not in [ '1','2','3','4','5']:
      print("You do not need to claculate! Get lost ")
      break

   if choice == "5":
      print("Why you called me ? huh!")
      break
   
   
   num1= float(input("Enter the first number: "))
   
   num2= float(input("Enter the second number: "))

   if choice == "1":
      result = sum(num1, num2)
   elif choice == "2":
      result = subtract(num1,num2)
   elif choice == "3":
      result = product(num1,num2)
   elif choice == "4":
      result = division(num1,num2)
   print(f"Result : {result}")
   break
