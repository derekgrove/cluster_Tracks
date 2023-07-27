# This function will calculate the "center of charge" exactly like you would center of mass.

def calculate_charge(cluster):
    total_charge = sum(charge for _, _, charge in cluster)

    xcharge = sum(x * charge for x, _, charge in cluster)
    ycharge = sum(y * charge for _, y, charge in cluster)

    x_coc = xcharge / total_charge
    y_coc = ycharge / total_charge

    coc = (x_coc, y_coc, total_charge)

    return coc
