# first input: enter height in inches
height_feet = int(input("Enter Your Height - Please enter the number of feet you are first\n")) * .3048
height_inches = int(input("Enter Your Height - Now enter the number of inches you are\n")) * .0254
total_height_meters = height_feet + height_inches
# print(total_height_meters)

# 2nd input: enter weight in pounds. it is converted into kilograms
weight_kilo = int(input("Please Enter Your Weight in Pounds\n")) * .453592
# print(weight_kilo)

bmi = weight_kilo / (total_height_meters ** 2)
print("\nYour BMI is: " + str(bmi) + "!")

