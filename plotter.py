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

def plot_cluster_zoomed(cluster, cluster_number, center_of_charge, min_angle, max_angle):
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

    plt.colorbar(label='Charge')
    plt.title('Cluster: ' + str(cluster_number))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(xmin, xmax+1, 1))
    plt.yticks(np.arange(ymin, ymax+1, 1))
    plt.grid(True)
    plt.show()
