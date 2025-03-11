#invite the user to input their weight and height as a string
weight_str = input("Enter your weight in kg: ")
height_str = input("Enter your height in m: ")

#transform string into number
weight = float(weight_str)
height = float(height_str)

#use the formula to calculate the bmi and set the value to a variable
bmi = weight/(height**2)

#if bmi is less than 18.5, output underweight; if bmi is larger than 30, output obese
if bmi < 18.5:
    print(f"Your bmi is {bmi}. Notice that you are likely underwwight, eat more!")
elif bmi > 30:
    print(f"Your bmi is {bmi}. Notice that you are obese, exercise more!")
else:
    print(f"Your bmi is {bmi}. Be happy that you have a normal weight.")