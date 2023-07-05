import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Generate data for the localized, elongated, and compressed Gaussian cluster
n_samples = 5000
mean = [128, 128]  # Mean of the cluster (centered within the histogram)
cov = [[20, 0], [0, 1]]  # Covariance matrix of the cluster (compressed in x and y directions)
cluster_data = np.random.multivariate_normal(mean, cov, n_samples)

# Extract x and y coordinates from the cluster data
x = cluster_data[:, 0]
y = cluster_data[:, 1]

# Create a 2D histogram
bins = 256  # Number of bins for x and y axes
hist, xedges, yedges = np.histogram2d(x, y, bins=bins, range=[[0, bins], [0, bins]])

# Plot the 2D histogram with a brighter colormap
plt.imshow(hist.T, origin='lower', extent=[0, bins, 0, bins], cmap='plasma')
plt.colorbar(label='Counts')
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(np.arange(0, bins+1, 50))  # Set x-axis ticks at intervals of 50
plt.yticks(np.arange(0, bins+1, 50))  # Set y-axis ticks at intervals of 50
plt.title('Cluster of Charge')
plt.show()


# Calculate the center of the cluster
center_x = np.mean(x)
center_y = np.mean(y)
