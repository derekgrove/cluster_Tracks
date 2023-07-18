import parse_data as parse
import center_charge as coc
import plotter as plt

min_cluster = int(input("Enter the starting cluster index: "))
max_cluster = int(input("Enter the ending cluster index: "))
zoomed_in = bool(input("Make zoomed in plots? (True, False):"))
def main():
    filename = 'raw_data.txt'
    truths, clusters = parse.parse_data(filename)
    center_of_charges = []
    for i in range(min_cluster, max_cluster+1):
        cluster = clusters[i]
        center_of_charge = coc.calculate_charge(cluster)
        center_of_charges.append(center_of_charge)
        if zoomed_in == True:
            plt.plot_cluster_zoomed(cluster)
        else:
            plt.plot_cluster(cluster)
    print("Center of charges: ", center_of_charges)


if __name__ == "__main__":
    main()

