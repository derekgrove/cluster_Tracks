#should sort through an array (256x256, size of pixel) and locate two things: skirt, core
#once those are found, should determine the major length and minor length
#maybe we remove the delta rays here as well, do this with with a morphology operator
def create_cluster(pixel_data, x, y):
    # Convert x, y to integers
    x = int(x)
    y = int(y)

    # Define the cluster list
    cluster = []

    # Iterate through the pixel data in steps of 3 (since each pixel's data is in three parts)
    for i in range(0, len(pixel_data), 3):
        px, py, charge = pixel_data[i:i+3]

        # Check if the pixel is within the specified range
        if (x - 1 <= px <= x + 1) and (y - 1 <= py <= y + 1):
            # If it is, append its data as a list to the cluster list
            pixel = [px, py, charge]
            cluster.append(pixel)

    return cluster

# Example usage:
#pixel_data = [76, 43, 1288558, 76, 44, 429279, 76, 45, 858705, 76, 46, 1288635, 77, 42, 1288458, 77, 43, 4386506, 77, 44, 15839894, 77, 45, 23389447, 77, 46, 8160435, 77, 47, 1288497, 78, 41, 429392, 78, 42, 1717826, 78, 43, 21853510, 78, 44, 82552974, 78, 45, 88274910, 78, 46, 19082788, 78, 47, 3865416, 78, 48, 429642, 79, 42, 1861333, 79, 43, 29853891, 79, 44, 123599631, 79, 45, 113251555, 79, 46, 33299005, 79, 47, 3670150, 79, 48, 429393, 80, 42, 1718036, 80, 43, 10492117, 80, 44, 35844701, 80, 45, 31129890, 80, 46, 8916696, 80, 47, 1288251, 81, 43, 2147723, 81, 44, 2863957, 81, 45, 3240776, 81, 46, 429472, 82, 44, 429536]
#x = 78.66152245649133
#y = 44.51666220841505

#cluster = create_cluster(pixel_data, x, y)
#print(cluster)
