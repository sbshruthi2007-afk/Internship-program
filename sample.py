secret_number = 7

guess = int(input("Guess the number (1-10): "))

if guess == secret_number:
    print("🎉 Correct!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")