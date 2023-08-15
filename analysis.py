import parse_data as parse
import center_charge as coc
import plotter as plt
import find_cluster as fc
import true_values as tv

min_cluster = int(input("Enter the starting cluster index: "))
max_cluster = int(input("Enter the ending cluster index: "))
zoomed_in = input("Make zoomed in plots? (yes, no): ").lower() == "yes"
charge_threshold = 10**2


def main():
    filename = 'raw_data.txt'
    truths, raw_data = parse.parse_data(filename)

    if min_cluster < 0 or max_cluster >= len(raw_data):
        print("Error: Invalid cluster range. Please make sure the min and max are within the range of raw_data.")
        return
    
    center_of_charges = []
    for i in range(min_cluster, max_cluster+1):
        cluster = raw_data[i]
        
        # Agglomerate pixels based on charge threshold
        cluster = fc.agglomerate_pixels(cluster, charge_threshold)

        # Plot charge histogram for the current cluster
        plt.plot_charge_histogram(cluster)
        
        true_beta = tv.calculate_true_beta(truths[i])
        #true_cluster_position = (truths[i][1], truths[i][2])
        center_of_charge = coc.calculate_charge(cluster)
        center_of_charges.append(center_of_charge)
        min_angle, max_angle = fc.find_optimal_angle(cluster, center_of_charge)

        if zoomed_in == True:
            plt.plot_cluster_zoomed(cluster, i, center_of_charge, min_angle, max_angle, true_beta)
        else:
            plt.plot_cluster(cluster, i, center_of_charge, min_angle, max_angle)

    print("min angle: " + str(min_angle))
    print("max angle: " + str(max_angle))
    #print("Center of charges: ", center_of_charges)
    #print(cluster)


if __name__ == "__main__":
    main()
