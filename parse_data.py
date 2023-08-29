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
                # Convert data to list of tuples (x, y, charge)
                cluster = [int(e) for e in elements[7:]]
                cluster = [(cluster[i], cluster[i+1], cluster[i+2]) for i in range(0, len(cluster), 3)]
                clusters.append(cluster)  # add the rest to the second list
            else: 
                continue
                
    return truths, clusters

