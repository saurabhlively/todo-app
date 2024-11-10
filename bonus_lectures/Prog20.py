try:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    if length == width:
        exit("It looks like square not rectangle")

    area = length * width
    print(area)
except ValueError:
    print("Enter numbers only")
