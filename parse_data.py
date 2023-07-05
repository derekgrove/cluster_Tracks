truths = []
clusters = []

with open('raw_data.txt', 'r') as f:
    lines = f.read().split('\n')  # split the file content by new lines

    for line in lines:
        elements = line.split(', ')  # split each line by a comma + space
        if len(elements) >= 7:  # check if the line has at least 5 elements
            truths.append([float(e) for e in elements[:7]])  # add first 5 elements to the first list
            clusters.append([int(e) for e in elements[7:]])  # add the rest to the second list
print("first list")
print(truths)
print("second list")
print(clusters)

# below line verifies that the variable type of every element in the second array is integers
# if a single element were not an integer then is_all_int would be set to False after going through the loop

#is_all_int = True
#for sublist in second_list:
#    for item in sublist:
#        if not isinstance(item, int):
#            is_all_int = False
#            break
#print(is_all_int)

# Our current format:
# index[0], type of particle: 0 = lithium, 1 = alpha
# index[1], cluster position in x
# index[2], cluster position in y
# index[3], local start X
# index[4], local start Y
# index[5], local end X
# index[6], local end Y
# then, by index[7], we start printing out the pixel values in an x, y, charge, x, y, charge... repeating pattern
# each new line is a new cluster
# since we will eventually not need these first 5 data points, I will split this data into two lists
# and when the time comes, we just remove all uses and instantiation of the first list
