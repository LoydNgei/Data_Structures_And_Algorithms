def data_type_size(type_str: str) -> int:
    data_types = {
        'Integer': 4,
        'Long': 8,
        'Float': 4,
        'Double': 8,
        'Character': 1
    }

    # Check if the provided type is in the dictionary
    if type_str in data_types:
        return data_types[type_str]
    else:
        # If the provided type is not in the dictionary, return -1 or any suitable value to indicate an error
        return -1

# Sample Input
input_type = input("Enter a data type: ")

# Get the size of the data type
size = data_type_size(input_type)

# Output the result
if size != -1:
    print(size)
else:
    print("Invalid data type.")
