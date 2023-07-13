# cluster_Tracks
 finding cluster positions and angle of particles from AllPix simulation


Our current format:
index[0], type of particle: 0 = lithium, 1 = alpha
index[1], cluster position in x
index[2], cluster position in y
index[3], local start X
index[4], local start Y
index[5], local end X
index[6], local end Y
index[7], we start printing out the pixel values in an x, y, charge, x, y, charge... 
this is a repeating pattern. Each new line is a new cluster since we will eventually not need these first 5 data points, I will split this data into two lists and when the time comes, we just remove all uses and instantiation of the first list

run analysis.py to run the entire program, it imports the other python files to get their functions.