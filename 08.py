check_string_lambda = lambda s: any(char.isupper() for char in s) and any(char.islower() for char in s) and any(char.isdigit() for char in s) and len(s) >= 10

input_string = "PaceWisd0m"
result = check_string_lambda(input_string)

if result:
    print("Valid string")
else:
    print("Invalid string")