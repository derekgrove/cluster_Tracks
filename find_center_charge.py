def calculate_charges(clusters):
    charges = []
    for cluster in clusters:
        charges.append([cluster[i] for i in range(2, len(cluster), 3)])

    total_charges = [sum(sublist) for sublist in charges]
    
    return total_charges
