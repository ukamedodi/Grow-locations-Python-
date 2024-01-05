# Grow-locations-Python-
This is my python assignment Repo to be submitted for marking. 

For this assignment I was provided with: The Grow dataset Growlocations.csv. This file contains the locations of all the GROWsensors as Latitude and Longitude.
A map of the UK from Openstreet map was provided .Using the map, I then created a Python program that can read the dataset into a dataframe and plot the locations of the sensors on the map provided. Having looked at the dataset there are a number of errors with the dataset that I needed to fix in order to get the correct plot. 

These include: Some location values are way outside the allowed values for latitude and Longitude. Some locations are not on the map provided. The labels of the columns have not be verified so may be incorrect.The bounding box for the map is as follows: {Longitude Min -10.592, Longitude Max 1.6848, Latitude Min 50.681, Latitude Max 57.985}

In order to fix the above problems, the code which i created has a bounding box and the logic here is to count the points in the box as valid and reject values outside the bounding box as irrelevant. 

For the columns the original csv file had Longitude and Latitude flipped so all i had to do was write a code to adjust this 


My code has been able to achive the following listed below: 

Reading the data into a data frame. with this line of code : (sensor_data = pd.read_csv('GrowLocations.csv')
Removing bad values. : this was achieved using the bounding box  code - fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(UK_map, extent=[-10.592, 1.6848, 50.681, 57.985], alpha=0.5)
Fixing other problems : sensor_data = sensor_data.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'}) here I labelled Longitude and Latitudes correctly to get the right points.
Plotting the data correctly : the code used here is the print function # Display a message indicating the successful save
print("Plot saved as {}".format(outputFileName)) also i took the extra step to make sure it prints the map as a Jpeg in the vscode workspace for the professor to have a look, mark and make comments and edits where necessary. 

Libraries used for this assignment were listed below. 
import pandas as pd ( for the general pyhton workspace)
import matplotlib.pyplot as plt (this was imported to plot the necessary graphs)
import os (for file operations) 
