# 1. Check a number is prime number or not
prime_number = int(input("Enter a number: "))
if prime_number > 1:
    for a in range(2, prime_number):
       if (prime_number % a) == 0:
           print(prime_number, "is not a prime number")
            
    else:
       print(prime_number, "is a prime number")
else:
    print(prime_number, "is not a prime number")
 
 
# 2. Check a number is armstrong number or not
number = int(input("Enter a number: "))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
temp //= 10

if number == sum:
    print(number, "is an Armstrong number")
else:
   print(number, "is not an Armstrong number")
        
#  3.  Print Fibonacci upto ten numbers
fibonacci_numbers = []  

for i in range(10):  
   number = int(input("Enter a number: "))
   fibonacci_numbers.append(number)

print(fibonacci_numbers)


# 4. Generate a list of twenty "four-digit" values and each values of the list must be unique

import random
new_list = []
while len(new_list) < 20:
    
   a = random.randint(1000, 9999) 
   if  a not in new_list:
      new_list.append(a)
    
      print(new_list)


# 5. Sort a list of number in ascending order with out using built in sort function


new_numbers = []
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)


sorted_numbers = []
while numbers:
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    sorted_numbers.append(smallest)
    numbers.remove(smallest)

print("Sorted list:", sorted_numbers)

# 6. Find the minimum value of number list without using builtin function

numbers = []


n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)


smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Minimum value:", smallest)


# 7.Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum

a = int(input("number a = "))
b = int(input ("number b ="))
product = a*b 
sum = a+b
if product <= 1000:
    print(product)
else:
    print(sum)

# 8.Iterate the numbers from one to ten, and in each iteration, print the sum of the current and previous number
for i in range(1, 11):
   if i == 1:
       previous_number = 0
else:
       previous_number = i - 1
current_number = i
sum_of_numbers = current_number + previous_number
print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum_of_numbers}")


# 9 .Create two arrays consists of number, if both arrays has same values, print or console log those values

array1 = input("Enter elements for array1 (space-separated): ").split()

array2 = input("Enter elements for array2 (space-separated): ").split()

common_values = []

for element in array1:
   
 if element in array2:
      
  common_values.append(element)
else:
      print(" there is no same value in both the arrays")


print("Common values:", common_values)

# 10. Check a word is palindrome or not
word = input("Enter a word: ")


reversed_word = word[::-1]


if word == reversed_word:
   print("The word is a palindrome.")
else:
   print("The word is not a palindrome.")

# 11) Check whether a number is in array or not
number = int(input("Enter a number: "))

array = [1, 2, 3, 4, 5]

if number in array:
   print(f"{number} is present in the array.")
else:
   print(f"{number} is not present in the array.")

# 12) Celcius to farenheit converter
celsius = int(input("Enter temperature in Celsius: "))

fahrenheit = 0
for i in range(celsius):
   fahrenheit += 1.8
print("Temperature in Fahrenheit:", fahrenheit)
                  # or using this method..
celsius = input("Enter temperature in Celsius: ")

# Convert Celsius to Fahrenheit
fahrenheit = int(celsius) * 9 // 5 + 32

print("Temperature in Fahrenheit:", fahrenheit)

# 13) Celcius to kelvin converter
celsius = int(input("Enter temperature in Celsius: "))

kelvin = 0
for i in range(celsius):
   kelvin += 1

print("Temperature in Kelvin:", kelvin)
               #  or
celsius = int(input("Enter temperature in Celsius: "))

# Convert Celsius to Kelvin
kelvin = 273 + (celsius // 1)

print("Temperature in Kelvin:", kelvin)



# 14) Print the series of numbers from 1 to the entered number
number = int(input("Enter a number: "))

for i in range(1, number+1):
   print(i)

# 15) Password generator
import random

number = int(input("Enter the length of the password: "))

if number <= 0:
    print("Invalid length. Please enter a positive number.")
else:
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""
    for i in range(number):
     password += random.choice(characters)
    
     print("Generated Password:", password)

#16 Username creator by getting the name, age and birthyear from user, write the code as a function

def create_username():
   name = input("Enter your name: ")
   age = int(input("Enter your age: "))
   birth_year = int(input("Enter your birth year: "))
   username = name + str(age) + str(birth_year)
   return username
username = create_username()
print("Your username is:", username)


#17) Bmi calculator
weight = int(input("Enter weight in kg: "))
height = int(input("Enter height in cm: "))

# Calculate BMI
BMI = 0

if height > 0:
   BMI = weight / ((height/100) ** 2)

print("BMI:", BMI)
   

       # or 
weight = int(input("Enter weight in kg: "))
height = int(input("Enter height in cm: "))

# Convert height from cm to meters


height_meters = height / 100

   
# Calculate BMI
bmi = weight / (height_meters ** 2)

print("BMI:", bmi)


#18) Loan emi calculator
principal = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
tenure = int(input("Enter tenure in months: "))

# Calculate monthly interest rate
monthly_interest_rate = interest_rate / 12 / 100

# Calculate EMI
emi = 0

if tenure > 0:
   numerator = 1
   denominator = 1

for _ in range(tenure):
       numerator *= (1 + monthly_interest_rate)
       denominator *= (1 + monthly_interest_rate)
emi = (principal * monthly_interest_rate * numerator) / (denominator - 1)

print("EMI:", emi)
print("your monthly laon amount is : ")
print(" your ")

                   # or 
principal = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
tenure = int(input("Enter tenure in months: "))

# Calculate monthly interest rate
monthly_interest_rate = interest_rate / 12 / 100

# Calculate EMI
emi = 0

if tenure > 0:
   emi = (principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure)) / (((1 + monthly_interest_rate) ** tenure) - 1)

print("EMI:", emi)



#19) Loan eligibility calculator

principal = input("Enter loan amount: ")
interest_rate = input("Enter annual interest rate (%): ")
tenure = input("Enter tenure in months: ")

# Check if inputs are valid numbers
if not principal.isdigit() or not interest_rate.isdigit() or not tenure.isdigit():
   print("Invalid input. Please enter valid numbers.")
else:
   principal = int(principal)
   interest_rate = int(interest_rate)
   tenure = int(tenure)

   #  Calculate monthly interest rate
   monthly_interest_rate = interest_rate / 12 / 100

   #  Calculate EMI
   emi = 0

   if tenure > 0:
     numerator = 1
     denominator = 1
   for _ in range(tenure):
           numerator *= (1 + monthly_interest_rate)
           denominator *= (1 + monthly_interest_rate)
           emi = (principal * monthly_interest_rate * numerator) // (denominator - 1)

#20) Create a chatbot for Samsung Mobile, where people can enquiry details about lastest mobile for purchasing

            
user_input = input("What would you like to know about the latest Samsung Mobile? (Type 'exit' to quit) ")

if  "price" in user_input.lower() :
       print("The price of the latest Samsung Mobile is $1000.")
elif"specs"in  user_input.lower():
       print("The specifications of the latest Samsung Mobile are high battery life , high camera quality")
elif "availability" in user_input.lower():
       print("The latest Samsung Mobile is currently available in all major stores.")
elif "quality" in user_input.lower():
       print("The latest Samsung Mobile is providing amazing quality.")
else:
       print("Sorry, I don't have information about that. Please ask something else.")

