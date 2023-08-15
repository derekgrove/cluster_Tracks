#should sort through an array (256x256, size of pixel) and locate two things: skirt, core
#once those are found, should determine the major length and minor length
#maybe we remove the delta rays here as well, do this with with a morphology operator
import numpy as np

def agglomerate_pixels(cluster, charge_threshold):
    # Initialize visited set and graph
    visited = set()
    graph = {(x, y): set() for x, y, _ in cluster}
    pixel_info = {(x, y): charge for x, y, charge in cluster}

    # Build graph
    for x, y, _ in cluster:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (x + dx, y + dy) in graph:
                    graph[(x, y)].add((x + dx, y + dy))

    # Depth-first search
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from the pixel with the highest charge
    start_node = max(cluster, key=lambda pixel: pixel[2])[:2]
    dfs(start_node)

    # Get the maximum charge in the cluster
    max_charge = max(pixel_info.values())

    # Filter the visited pixels based on the charge threshold
    filtered_pixels = [[x, y, pixel_info[(x, y)]] for x, y in visited if pixel_info[(x, y)] >= max_charge / charge_threshold]

    return filtered_pixels


def line_intersection_length(x1, y1, x2, y2, px, py, size=1):
    """Calculate the intersection length of a line segment with a pixel."""
    from shapely.geometry import LineString, box

    line = LineString([(x1, y1), (x2, y2)])
    pixel = box(px - size/2, py - size/2, px + size/2, py + size/2)

    if not line.intersects(pixel):
        return 0

    intersection = line.intersection(pixel)
    if intersection.geom_type == 'LineString':
        return intersection.length
    elif intersection.geom_type == 'MultiLineString':
        return sum(seg.length for seg in intersection)
    else:  # Point
        return 0


def find_optimal_angle(cluster, center_of_charge):
    center_x, center_y, _ = center_of_charge

    # Define the length of the line
    line_length = 50

    # Define a list to store the total charge for each angle
    total_charges = []

    # For each angle from 0 to 360 degrees with a step of 0.01
    for angle in np.arange(0, 360, 0.01):
        # Calculate the coordinates of the line
        dx = line_length * np.cos(np.radians(angle))
        dy = line_length * np.sin(np.radians(angle))

        # Determine the start and end points of the line
        x1, y1 = center_x - dx, center_y - dy
        x2, y2 = center_x + dx, center_y + dy

        # Check each pixel in the cluster
        total_charge = 0
        for x, y, charge in cluster:
            # Determine if the pixel is intersected by the line
            d = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / np.sqrt((y2 - y1)**2 + (x2 - x1)**2)
            if d < 0.5:
                total_charge += charge

        total_charges.append(total_charge)

    # Find the maximum total charge
    max_charge = max(total_charges)

    # Find the angles that yield the maximum total charge
    optimal_angles = [angle for angle, total_charge in zip(np.arange(0, 360, 0.01), total_charges) if total_charge == max_charge]

    # Return the minimum and maximum optimal angles
    return min(optimal_angles), max(optimal_angles)

def find_optimal_angle_new(cluster, center_of_charge):
    center_x, center_y, _ = center_of_charge

    # Define the length of the line
    line_length = 50

    # Define a list to store the total scaled charge for each angle
    total_scaled_charges = []

    # For each angle from 0 to 360 degrees with a step of 0.01
    for angle in np.arange(0, 360, 0.01):
        # Calculate the coordinates of the line
        dx = line_length * np.cos(np.radians(angle))
        dy = line_length * np.sin(np.radians(angle))

        # Determine the start and end points of the line
        x1, y1 = center_x - dx, center_y - dy
        x2, y2 = center_x + dx, center_y + dy

        # Check each pixel in the cluster
        total_scaled_charge = 0
        for x, y, charge in cluster:
            length = line_intersection_length(x1, y1, x2, y2, x, y)
            total_scaled_charge += charge * length

        total_scaled_charges.append(total_scaled_charge)

    # Find the maximum total scaled charge
    max_scaled_charge = max(total_scaled_charges)

    # Find the angles that yield the maximum total scaled charge
    optimal_angles = [angle for angle, total_scaled_charge in zip(np.arange(0, 360, 0.01), total_scaled_charges) if total_scaled_charge == max_scaled_charge]

    # Return the minimum and maximum optimal angles
    return min(optimal_angles), max(optimal_angles)

