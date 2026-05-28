def calculate_bill(height, age, wants_photo):
    if height < 120:
        return None
    bill = 5 if age < 12 else 7 if age <= 18 else 12
    if wants_photo:
        bill += 3
    return bill


if __name__ == "__main__":
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        photo = input("Do you want a photo taken? Y or N. ")
        bill = calculate_bill(height, age, photo == "Y")
        print(f"Please pay ${bill}.")
    else:
        print("Sorry, you have to grow taller before you can ride.")