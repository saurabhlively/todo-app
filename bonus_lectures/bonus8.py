date = input("Enter today's date: ")
mood = input("Please rate ur mood from 1 to 10 : ")
thoughts = input("Enter your thoughts flow:\n ")

with open(f"journal/{date}.txt",'w') as file:
    file.write(mood + 2* "\n")
    file.write(thoughts)


