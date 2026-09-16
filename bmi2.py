height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

if height <= 0 or weight <= 0:
	print("Height and weight must be greater than zero.")
else:
	bmi = weight / (height * height)
	print(f"Your BMI is: {bmi:.2f}")

	if bmi < 18.5:
		print("You are underweight.")
	elif bmi < 25:
		print("You have a normal weight.")
	elif bmi < 30:
		print("You are overweight.")
	else:
		print("You are obese.")
