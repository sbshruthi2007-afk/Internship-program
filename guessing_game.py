def guessing_game():
    s=55
    while True:
        try:
            num=int(input("Enter the number:"))
        except:
            print("Invalid Input")
            continue
        if num>s:
            print("High,Try guessing low")
        elif num<s:
            print("Low,Try guessing high")
        else:
            print("Great, Found the number")
            break
guessing_game()