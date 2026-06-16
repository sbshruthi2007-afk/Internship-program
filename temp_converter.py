
print("Temperature Converter")
print("1.Celsius To Fahrenheit")
print("2.Fahrenheit To Celsius")
choice=int(input("Enter the Choice(1 or 2):"))
if choice==1:
    celsius=float(input("Enter the temperature in celsius:"))
    fahrenheit=(celsius*9/5)+32
    print(f"{celsius}C={fahrenheit:.2f}F")
elif choice==2:
    fahrenheit=float(input("Enter the temperature in fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print(f"{fahrenheit}F={celsius:.2f}C")
else:
    print("Invalid choice")