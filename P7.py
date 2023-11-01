def find_string_indices(input_list):
    indices = [str(i) for i, item in enumerate(input_list) if isinstance(item, str)]
    return ''.join(indices)

input_list = ['Navya', 98, 'Hema', 'Siroj', 'Tarun', 78, 90, "Ramya"]
output = find_string_indices(input_list)
print(output)
