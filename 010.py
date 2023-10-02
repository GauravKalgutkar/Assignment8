original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

sorted_list = sorted(original_list, key=lambda x: (isinstance(x, int), x))
print("Sort the mixed list of integers and strings:", sorted_list)