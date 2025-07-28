#BMI calculation program
weight= float(input("Enter your body weight in kg: "))
height= float(input ("Enter your body height in feet: "))
height_in_feet=height*0.3048
BMI= weight/(height_in_feet**2)
print (f" Your BMI is={BMI} ")
if  (BMI<18.5):
    print( "You are underweight")
elif (BMI>=18.5 and BMI<=24.9):
    print("Your weight is normal")
elif (BMI>=30 and BMI<=34.9):
    print("You are an obese")
else:
    print ("You are extemely obese")
