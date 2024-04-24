
feet = eval(input("Enter a value for feet: "))
print(feet, "feet is", round(feet*0.305,4), "meters")

pounds = eval(input("Enter a value in pounds: "))
print(pounds, "pounds is", round(pounds*0.454,3), "kilograms")

subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate: "))
print("The gratuity is", round(subtotal * gratuity/100,2), "and the total is", round(subtotal+subtotal*gratuity/100,2))

amount = eval(input("Enter the amount of water in kilograms: "))
initial = eval(input("Enter the initial temperature: "))
final = eval(input("Enter the final temperature: "))
print("The energy needed is", amount * (final - initial) * 4184)