def calculate_charges(clusters):
    center_of_charge = []
    charges = []
    xs = []
    ys = []
    for cluster in clusters:
        xs.append([cluster[i] for i in range(0, len(cluster), 3)])
        ys.append([cluster[i] for i in range(1, len(cluster), 3)])
        charges.append([cluster[i] for i in range(2, len(cluster), 3)])

    total_charge = [sum(sublist) for sublist in charges]

    xcharge = []
    ycharge = []

    # For each pair of sublists
    for sub_xs, sub_charges in zip(xs, charges):
        # Calculate the sum of x[i] * charge[i] and append it to xcharge
        xcharge.append(sum(x * charge for x, charge in zip(sub_xs, sub_charges)))

    for sub_ys, sub_charges in zip(ys, charges):
        # Calculate the sum of y[i] * charge[i] and append it to ycharge
        ycharge.append(sum(y * charge for y, charge in zip(sub_ys, sub_charges)))

    #define center of charge for x and y:
    x_coc = []
    y_coc = [] 

    for i in range(len(total_charge)):
        x_coc.append(xcharge[i] / total_charge[i])
        y_coc.append(ycharge[i] / total_charge[i])

    coc = list(zip(x_coc, y_coc, total_charge))

    return coc