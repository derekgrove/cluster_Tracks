# Organize the data into two separate arrays, the first array is knowledge we won't have access to from experiment, its just values from the simulation we can use to check our work.
def parse_data(filename):
    truths = []
    clusters = []

    with open(filename, 'r') as f:
        lines = f.read().split('\n')  # split the file content by new lines

        for line in lines:
            elements = line.split(', ')  # split each line by a comma + space
            if len(elements) >= 7:  # check if the line has at least 7 elements
                truths.append([float(e) for e in elements[:7]])  # add first 7 elements to the first list
                clusters.append([int(e) for e in elements[7:]])  # add the rest to the second list
            else: 
                continue
                
    return truths, clusters
