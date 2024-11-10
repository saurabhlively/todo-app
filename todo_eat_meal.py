toeat = []

while True:
    user_input=input("Enter the action after going thru meal menu").strip()
    match user_input:
        case 'serve_meal':
            eat = input("Enter the meal you want to eat")
            toeat.append(eat)
        case 'display_meal':
            for meals in toeat:
                print(meals)
        case 'exit':
            break
        case _:
            print("this is not a valid input")
            break

print("Bye")
