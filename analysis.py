import parse_data as parse
import center_charge as coc
import plotter as plt
import find_cluster as fc
import true_values as tv
from scipy.stats import skew

min_cluster = int(input("Enter the starting cluster index: "))
max_cluster = int(input("Enter the ending cluster index: "))
pixel_plots = input("Make pixel plots? (yes, no): ").lower() == "yes"

if pixel_plots:
    zoomed_in = input("Make zoomed in plots? (yes, no): ").lower() == "yes"
else:
    zoomed_in = False

charge_threshold = 10**20

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
        
        # Calculate skewness for the x and y distributions of the trimmed cluster
        x_values = [pixel[0] for pixel in cluster]
        y_values = [pixel[1] for pixel in cluster]
        x_skewness = skew(x_values)
        y_skewness = skew(y_values)
        
        # Plot histograms for x and y distributions
        plt.plot_pixel_histograms(x_values, y_values, i)
        plt.plot_charge_histograms(cluster, i)
        print(f"Skewness in x-direction for cluster {i}: {x_skewness:.4f}")
        print(f"Skewness in y-direction for cluster {i}: {y_skewness:.4f}")

        if pixel_plots:
            true_beta = tv.calculate_true_beta(truths[i])
            center_of_charge = coc.calculate_charge(cluster)
            center_of_charges.append(center_of_charge)
            min_angle, max_angle = fc.find_optimal_angle(cluster, center_of_charge)
            
            if zoomed_in:
                plt.plot_cluster_zoomed(cluster, i, center_of_charge, min_angle, max_angle, true_beta)
            else:
                plt.plot_cluster(cluster, i, center_of_charge, min_angle, max_angle)

    if pixel_plots:
        print("min angle: " + str(min_angle))
        print("max angle: " + str(max_angle))
        print("Center of charges: ", center_of_charges)
    print(cluster)

if __name__ == "__main__":
    main()
