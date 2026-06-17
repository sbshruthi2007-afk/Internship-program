from utlis import celsius_to_fahrenheit
from utlis import fahrenheit_to_celsius
print("Temperature Converter")
print("1.Celsius To Fahrenheit")
print("2.Fahrenheit To Celsius")
choice=int(input("Enter the Choice(1 or 2):"))
if choice==1:
    celsius=float(input("Enter the temperature in celsius:"))
    print(celsius_to_fahrenheit(celsius))
elif choice==2:
    fahrenheit=float(input("Enter the temperature in fahrenheit:"))
    print(fahrenheit_to_celsius(fahrenheit))
else:
    print("Invalid choice")