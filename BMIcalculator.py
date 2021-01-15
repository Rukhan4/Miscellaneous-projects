# Welcoming message
print('Welcome to the bmi calculator')
user = str(input("What's your name?:"))
print('\n')
# Declaring unit as empty
unit = ''
while not unit:
    unit = str(input("Chose 1 for imperial and 2 for metric units(1/2):"))
    if unit in ["1", "2"]:
        if unit == "1":
            print('You have chosen imperial units')
            heighti = float(input('Please enter your height in inches:'))
            weighti = float(input('Now please enter your weight in lbs:'))
            bmi = ((weighti / (heighti**2) * 703))
        elif unit == "2":
            print('You have chosen metric units')
            heightm = float(input('Please enter your height in metres:'))
            weightm = float(input('Please enter your weight in kg:'))
            bmi = (weightm / (heightm**2))

        print(f'Your BMI is {bmi}')
        if ( bmi < 16):
            print("You are severely underweight")
            print("Suggestion: Mass gainers and high surplus of calories, consider strength training programs!")
        
        elif ( bmi >= 16 and bmi < 18.5):
            print("You are underweight")
            print("Suggestion:Medium surplus of calories, less cardio and more strength training!")
        
        elif ( bmi >= 18.5 and bmi < 25):
            print("You are Healthy")
            print("Suggestion: Keep it up!")

        elif ( bmi >= 25 and bmi < 30):
            print("You are overweight")
            print("Suggestion: Maintain a small caloric deficit of <250 calories and include cardio sessions!")
        
        elif ( bmi >=30):
            print("You are severely overweight")
            print("Suggestion: Maintain a greater caloric defiti of around 500 calories and consider HIIT training!")
    else:
        print('Not in range of choices')
        unit = ''
        continue
    

