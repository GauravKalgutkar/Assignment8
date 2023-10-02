original_list = ['red', 'black', 'white', 'green', 'orange']
substring = "ack"

filtered_list = list(filter(lambda s: substring in s, original_list))
print("Elements containing the specific substring:", filtered_list)