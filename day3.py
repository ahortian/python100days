MIN_HEIGHT_CM = 120
TICKET_PRICES = {"child": 5, "teen": 7, "adult": 12}
PHOTO_FEE = 3


def calculate_bill(height: int, age: int, wants_photo: bool) -> int | None:
    """Return the total bill in dollars, or None if the rider is too short."""
    if height < MIN_HEIGHT_CM:
        return None
    if age < 12:
        bill = TICKET_PRICES["child"]
    elif age <= 18:
        bill = TICKET_PRICES["teen"]
    else:
        bill = TICKET_PRICES["adult"]
    if wants_photo:
        bill += PHOTO_FEE
    return bill


def main() -> None:
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= MIN_HEIGHT_CM:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        photo = input("Do you want a photo taken? Y or N. ")
        bill = calculate_bill(height, age, photo == "Y")
        print(f"Please pay ${bill}.")
    else:
        print("Sorry, you have to grow taller before you can ride.")


if __name__ == "__main__":
    main()
