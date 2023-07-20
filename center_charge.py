# This function will calculate the "center of charge" exactly like you would center of mass.

def calculate_charge(cluster):
    xs = [cluster[i] for i in range(0, len(cluster), 3)]
    ys = [cluster[i] for i in range(1, len(cluster), 3)]
    charges = [cluster[i] for i in range(2, len(cluster), 3)]

    total_charge = sum(charges)

    xcharge = sum(x * charge for x, charge in zip(xs, charges))
    ycharge = sum(y * charge for y, charge in zip(ys, charges))

    x_coc = xcharge / total_charge
    y_coc = ycharge / total_charge

    coc = (x_coc, y_coc, total_charge)

    return coc
