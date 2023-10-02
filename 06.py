original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

divisible_lambda = lambda x: x % 19 == 0 or x % 13 == 0

result = list(filter(divisible_lambda, original_list))
print("Numbers divisible by nineteen or thirteen:", result)