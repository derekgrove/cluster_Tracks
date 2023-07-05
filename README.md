# cluster_Tracks
 finding cluster positions and angle of particles from AllPix simulation


Our current format:<br>
index[0], type of particle: 0 = lithium, 1 = alpha<br>
index[1], cluster position in x<br>
index[2], cluster position in y<br>
index[3], local start X<br>
index[4], local start Y<br>
index[5], local end X<br>
index[6], local end Y<br>
index[7], we start printing out the pixel values in an x, y, charge, x, y, charge... <br>
this is a repeating pattern. Each new line is a new cluster since we will eventually not need these first 5 data points, I will split this data into two lists and when the time comes, we just remove all uses and instantiation of the first list
