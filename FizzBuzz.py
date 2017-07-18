
#fizzbuzz function
def fizzbuzz(number):
    if mod(number, 15):
        return("FizzBuzz")
    elif mod(number, 5):
        return("Fizz")
    elif mod(number, 3):
        return("Buzz")
    else:
        return(":(")

#mod function
def mod(number1, number2):
    if number1 % number2 == 0:
        return True
    else:
        return False
"""
#age input example
age = int(input("How old are you? "))

if age <= 12:
    print("You are a smol child.")
elif age <= 18:
    print("Youngsters these days...")
else:
    print("You're ooooooooold!")

#fizzbuzz, without a function
number = int(input("Enter a number. "))

if number % 15 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Fizz")
elif number % 3 == 0:
    print("Buzz")
else:
    print(":(")

"""

#while loop
check = input("FizzBuzz? y/n ")

while check == "y":
    number = input("Enter a number. ")
    if number.isnumeric():
        number = int(number)
        result = fizzbuzz(number)
        print(result)
        check = input("Keep going? y/n ")
    else:
        print("That is not a number.")
