# first input: enter height in inches
height_feet = int(input("What is Your Height? - How many feet Feet are you\n"))
height_inches = int(input("What is Your Height - How many inches\n"))
print("You are " + str(height_feet) + '"' + str(height_inches) + "'!" )

conv_height_ft = height_feet * .3048
conv_height_inches = height_inches * .0254
total_height_meters = conv_height_ft + conv_height_inches
# print(total_height_meters)

# 2nd input: enter weight in pounds. it is converted into kilograms
weight_kilo = int(input("Please Enter Your Weight in Pounds\n")) * .453592
# print(weight_kilo)

bmi = weight_kilo / (total_height_meters ** 2)
print("\nYour BMI is: " + str(bmi) + "!")
