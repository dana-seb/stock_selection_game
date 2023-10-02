age = int(input("What is your age?\n"))

weeks_yr = 52

life_span = 90 * weeks_yr

user_current = age * weeks_yr

weeks_left = life_span - user_current

print(f"You have {weeks_left} weeks left.")