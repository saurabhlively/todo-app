#Group of similar items --> List
#Group of different items --> Dictionary
password = input("Enter the password: ")

result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True


result["digits"] = digit


uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercases"] = uppercase


if all(result.values()) == True:
    print("Strong password")
else:
    print("Weak password")

print(result)