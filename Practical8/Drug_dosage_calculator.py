# import necessary library
import numpy as np

# input the required data
# for children, the recommended dose of the painkiller is 15mg/kg
def calculator(weight, strength):
    """
    Input: x, weight; y, strength;
    Return: recommended dose of paracetamol
    """
    temp = True
    try:
        weight = int(weight)
    except ValueError:
        print("Your input for weight is incorrect. It should be an integer.")
        temp = False

    # deliver an error if the weight is beyond the range
    if temp:
        if weight < 10:
            print("Your child is too small to take painkiller paracetamol.")
            temp = False
        elif weight > 100:
            print("The dose is so large that it may have a potential toxic dose.")
            temp = False

    # deliver an error if the strength doesn't match the concentration
    if temp:
        if strength == "120mg/5ml":
            strength = 120 / 5
        elif strength == "250mg/5ml":
            strength = 250 / 5
        else:
            print("Your input doesn't match the expected concentration.")
            temp = False

    if temp:
        return (weight * 15) / strength


weight = input("Enter your weight in kg (10~100): ")
strength = input("Choose one strength of paracetamol (120mg/5ml or 250mg/5ml): ")
recommended = calculator(weight, strength)
if recommended is not None:
    print(f"Your recommended volume is {recommended} ml.")