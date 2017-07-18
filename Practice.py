blastoff = "Blastoff!"

#Method 1: using no variables
for number in range(-5,0):
    number = number*-1
    print(number)
print(blastoff)

#Method 2: uses a variable
variable = 6
for number in range(5):
    variable = variable - 1
    print(variable)
print(blastoff)

#Method 3: uses a while loop
count = 5
while (count > 0):
    print(count)
    count = count - 1
print(blastoff)

#On the whiteboard:

#condition-controlled
timeLeft = 5
while timeLeft > 0:
    print(timeLeft)
    timeLeft = timeLeft - 1
print("Blastoff!")

#counter-controlled
timeLeft = 5
for i in range(5):
    print(timeLeft)
    timeLeft = timeLeft - 1
print("Blastoff!")

for i in range(5,0,-1):
    print(i)
print("Blastoff!")
