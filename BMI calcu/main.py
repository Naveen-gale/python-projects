height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
height = height/100
bmi = weight / (height ** 2)

print("Your BMI is: ", bmi)
if bmi>0:
     if bmi <= 16:
            print("You are Severely underweight")
     elif bmi <= 16.9:
           print("You are Underweight")
     elif bmi <=25:
              print("You are Normal")
     elif bmi <= 30:
            print("You are Overweight")

