import parse_data as parse
import center_charge as coc
import plotter as plt
import find_cluster as fc

min_cluster = int(input("Enter the starting cluster index: "))
max_cluster = int(input("Enter the ending cluster index: "))
zoomed_in = bool(input("Make zoomed in plots? (True, False):"))
def main():
    filename = 'mini_data.txt'
    truths, clusters = parse.parse_data(filename)
    center_of_charges = []
    cluster_iter = []
    for i in range(min_cluster, max_cluster+1):
        cluster_iter.append(clusters[i])
        cluster = clusters[i]
        center_of_charge = coc.calculate_charge(cluster)
        center_of_charges.append(center_of_charge)
        if zoomed_in == True:
            plt.plot_cluster_zoomed(cluster)
        else:
            plt.plot_cluster(cluster)
    print("Center of charges: ", center_of_charges)
    print(cluster_iter)

    #for i in range(center_of_charge):
    #    cluster = fc.create_cluster(clusters, center_of_charge[i+3], center_of_charge[i+4])
    #    print(cluster)

if __name__ == "__main__":
    main()

