import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt

def plot_cluster(cluster):
    xs = [cluster[i] for i in range(0, len(cluster), 3)]
    ys = [cluster[i] for i in range(1, len(cluster), 3)]
    charges = [cluster[i] for i in range(2, len(cluster), 3)]

    xmin = min(xs) - 3
    xmax = max(xs) + 3
    ymin = min(ys) - 3
    ymax = max(ys) + 3

    
    plt.hist2d(xs, ys, weights=charges, cmap='magma', bins=[range(256), range(256)])
    plt.colorbar(label='Charge')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(xmin, xmax+1, 1))
    plt.yticks(np.arange(ymin, ymax+1, 1))
    plt.grid(True)
    plt.show()

def plot_cluster_zoomed(cluster):
    xs = [cluster[i] for i in range(0, len(cluster), 3)]
    ys = [cluster[i] for i in range(1, len(cluster), 3)]
    charges = [cluster[i] for i in range(2, len(cluster), 3)]

    xmin = min(xs) - 3
    xmax = max(xs) + 3
    ymin = min(ys) - 3
    ymax = max(ys) + 3

    
    histogram, xedges, yedges = np.histogram2d(xs, ys, weights=charges, bins=[range(xmin, xmax+1), range(ymin, ymax+1)])

    plt.pcolormesh(xedges, yedges, histogram.T, norm=colors.LogNorm(), cmap='magma')
    plt.colorbar(label='Charge')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(xmin, xmax+1, 1))
    plt.yticks(np.arange(ymin, ymax+1, 1))
    plt.grid(True)
    plt.show()

    