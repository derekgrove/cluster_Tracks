first_list = []
second_list = []

with open('mini_data.txt', 'r') as f:
    lines = f.read().split('\n')  # split the file content by new lines

    for line in lines:
        elements = line.split(', ')  # split each line by a comma + space
        if len(elements) >= 7:  # check if the line has at least 5 elements
            first_list.append([float(e) for e in elements[:7]])  # add first 5 elements to the first list
            second_list.append([int(e) for e in elements[7:]])  # add the rest to the second list
print("first list")
print(first_list)
print("second list")
print(second_list)

# below line verifies that the variable type of every element in the second array is integers
# if a single element were not an integer then is_all_int would be set to False after going through the loop

#is_all_int = True
#for sublist in second_list:
#    for item in sublist:
#        if not isinstance(item, int):
#            is_all_int = False
#            break
#print(is_all_int)