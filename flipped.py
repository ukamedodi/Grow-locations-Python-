# For the first line of code here i am importing the pandas library for data manipulation and matplotlib.pyplot for plotting the points 
import pandas as pd
import matplotlib.pyplot as plt
import os #file operations 

# The next step is to load the GrowLocationsData from a CSV file into a DataFrame for sensor location information
sensor_data = pd.read_csv('GrowLocations.csv')

# Here I renamed the latitude and longitude columns to ensure consistency in naming conventions as there was an error with the original csv
# so switching them was necessary. 
sensor_data = sensor_data.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})

# Now i Created a list of tuples containing latitude and longitude pairs for each sensor
# for the explanation above this list will be used to plot the sensor locations on the map
sensor_coordinates = [(row['Longitude'], row['Latitude']) for _, row in sensor_data.iterrows()]

# Now I am Loading the map image of the UK to be used as a background for the plot with line of code below
UK_map = plt.imread('map7.png')

#  the line of code below is creating a scatter plot with the specified map extent
#here is where i gave the limitations for the bounds. Having a bounding box is a form of cleaning the data removing unwanted locations outside 
# the United Kingdom. By doing this we get the specific points.
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(UK_map, extent=[-10.592, 1.6848, 50.681, 57.985], alpha=0.5)

# Plotting each sensor location as a blue dot on the map
ax.scatter(*zip(*sensor_coordinates), color='blue', s=12)

# over here I customized the plot with a title, x-axis label, and y-axis label
plt.title('GROW Sensor Locations on UK Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# now i set the x-axis and y-axis limits to match the specified map extent
plt.xlim(-10.592, 1.6848)
plt.ylim(50.681, 57.985)

# Display the plot
# plt.show()

# Specify the output filename
outputFileName = 'EDODI_output_visualisation.jpeg'

# Save the plot in the current directory, overwriting if it already exists
fig.savefig(outputFileName)

# Display a message indicating the successful save
print("Plot saved as {}".format(outputFileName)) 