import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt

def plot_cluster(cluster, cluster_number, center_of_charge, min_angle, max_angle):
    xs = [pixel[0] for pixel in cluster]
    ys = [pixel[1] for pixel in cluster]
    charges = [pixel[2] for pixel in cluster]

    coc_x, coc_y, _ = center_of_charge
    line_length = max(max(xs)-min(xs), max(ys)-min(ys)) / 2  # half the length of the line

    plt.hist2d(xs, ys, weights=charges, cmap='magma', bins=[range(256), range(256)])
    plt.colorbar(label='Charge')

    # Calculate the points for the min angle line
    min_angle_rad = np.deg2rad(min_angle)  # Convert to radians
    x1 = coc_x + line_length * np.cos(min_angle_rad)
    y1 = coc_y + line_length * np.sin(min_angle_rad)
    x2 = coc_x - line_length * np.cos(min_angle_rad)
    y2 = coc_y - line_length * np.sin(min_angle_rad)
    plt.plot([x1, x2], [y1, y2], 'b-')  # Plot the line for the min angle

    # Calculate the points for the max angle line
    max_angle_rad = np.deg2rad(max_angle)  # Convert to radians
    x1 = coc_x + line_length * np.cos(max_angle_rad)
    y1 = coc_y + line_length * np.sin(max_angle_rad)
    x2 = coc_x - line_length * np.cos(max_angle_rad)
    y2 = coc_y - line_length * np.sin(max_angle_rad)
    plt.plot([x1, x2], [y1, y2], 'r-')  # Plot the line for the max angle

    plt.title('Cluster: ' + str(cluster_number))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(False)
    plt.show()

def plot_cluster_zoomed(cluster, cluster_number, center_of_charge, min_angle, max_angle, true_beta):
    xs = [pixel[0] for pixel in cluster]
    ys = [pixel[1] for pixel in cluster]
    charges = [pixel[2] for pixel in cluster]

    xmin = min(xs) - 3
    xmax = max(xs) + 3
    ymin = min(ys) - 3
    ymax = max(ys) + 3

    histogram, xedges, yedges = np.histogram2d(xs, ys, weights=charges, bins=[range(xmin, xmax+1), range(ymin, ymax+1)])

    plt.pcolormesh(xedges, yedges, histogram.T, norm=colors.LogNorm(), cmap='magma')

    coc_x, coc_y, _ = center_of_charge
    #true_cluster_x, true_cluster_y = true_cluster_position
    line_length = max(xmax-xmin, ymax-ymin) / 2  # half the length of the line

    # Calculate the points for the min angle line
    min_angle_rad = np.deg2rad(min_angle)  # Convert to radians
    x1 = coc_x + line_length * np.cos(min_angle_rad)
    y1 = coc_y + line_length * np.sin(min_angle_rad)
    x2 = coc_x - line_length * np.cos(min_angle_rad)
    y2 = coc_y - line_length * np.sin(min_angle_rad)
    plt.plot([x1, x2], [y1, y2], 'b-')  # Plot the line for the min angle

    # Calculate the points for the max angle line
    max_angle_rad = np.deg2rad(max_angle)  # Convert to radians
    x1 = coc_x + line_length * np.cos(max_angle_rad)
    y1 = coc_y + line_length * np.sin(max_angle_rad)
    x2 = coc_x - line_length * np.cos(max_angle_rad)
    y2 = coc_y - line_length * np.sin(max_angle_rad)
    plt.plot([x1, x2], [y1, y2], 'r-')  # Plot the line for the max angle

    true_beta_rad = np.deg2rad(true_beta)  # Convert to radians
    x1 = coc_x + line_length * np.cos(true_beta_rad)
    y1 = coc_y + line_length * np.sin(true_beta_rad)
    x2 = coc_x - line_length * np.cos(true_beta_rad)
    y2 = coc_y - line_length * np.sin(true_beta_rad)
    plt.plot([x1, x2], [y1, y2], 'g--')

    plt.colorbar(label='Charge')
    plt.title('Cluster: ' + str(cluster_number))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(xmin, xmax+1, 1))
    plt.yticks(np.arange(ymin, ymax+1, 1))
    plt.grid(True)
    plt.scatter(coc_x, coc_y, color='black', zorder=3, marker='x')
    #plt.scatter(true_cluster_x, true_cluster_y, color='red', zorder=2, marker='+')
    plt.show()

def plot_z(start_x, start_y, end_x, end_y):
     
    delta_y = end_y - start_y
    delta_x = end_x - start_x

def plot_charge_histograms(cluster, cluster_number):
    # Initialize dictionaries to hold the charge values for each x and y coordinate
    charge_x = {}
    charge_y = {}

    # Populate the charge_x and charge_y dictionaries
    for x, y, charge in cluster:
        if x not in charge_x:
            charge_x[x] = 0
        if y not in charge_y:
            charge_y[y] = 0
        charge_x[x] += charge
        charge_y[y] += charge

    # Prepare the data for plotting
    x_coords, x_charges = zip(*sorted(charge_x.items()))
    y_coords, y_charges = zip(*sorted(charge_y.items()))

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Calculate bins for x and y
    x_bins = np.arange(min(x_coords), max(x_coords) + 2) - 0.5
    y_bins = np.arange(min(y_coords), max(y_coords) + 2) - 0.5

    # Plot charge distribution in x
    axs[0].hist(x_coords, weights=x_charges, bins=x_bins, edgecolor='black', alpha=0.7)
    axs[0].set_title(f'Charge Distribution in x for Cluster {cluster_number}')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Total Charge')

    # Plot charge distribution in y
    axs[1].hist(y_coords, weights=y_charges, bins=y_bins, edgecolor='black', alpha=0.7)
    axs[1].set_title(f'Charge Distribution in y for Cluster {cluster_number}')
    axs[1].set_xlabel('y')
    axs[1].set_ylabel('Total Charge')

    plt.tight_layout()
    plt.show()



def plot_pixel_histograms(x_values, y_values, cluster_number):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    # Calculate bins for x and y
    x_bins = np.arange(min(x_values), max(x_values) + 2) - 0.5
    y_bins = np.arange(min(y_values), max(y_values) + 2) - 0.5
    
    # Plot histogram for x-values
    axs[0].hist(x_values, bins=x_bins, edgecolor='black', alpha=0.7)
    axs[0].set_title(f'Pixel Distribution in x for Cluster {cluster_number}')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Frequency')
    
    # Plot histogram for y-values
    axs[1].hist(y_values, bins=y_bins, edgecolor='black', alpha=0.7)
    axs[1].set_title(f'Pixel Distribution in y for Cluster {cluster_number}')
    axs[1].set_xlabel('y')
    axs[1].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()
