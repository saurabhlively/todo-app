from converters14 import convert
from parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed['feet']} and {parsed['inches']} is equal to {result}")
if result > 1:
    print("Kid is big")
else:
    print("Kid is small")


