height=input("Enter the height in m:\n")
weight=input("Enter the weight in kg:\n")
bmi=float(weight)/float(height)**2
formatted_bmi=f"{bmi:.2f}"

if bmi<18.5:
    print(f"Your bmi is {formatted_bmi}, you are underweight.")
elif bmi<25:
    print(f"Your bmi is {formatted_bmi}, you have a normal weight.")
elif bmi<30:
    print(f"Your bmi is {formatted_bmi}, you are slightly overweight.")
elif bmi<35:
    print(f"Your bmi is {formatted_bmi}, you are obese")
else:
    print(f"Your bmi is {formatted_bmi}, you are clinically obese.")