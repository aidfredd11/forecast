import matplotlib.pyplot as plt
import numpy as np

# Define the time series data
time = np.arange(1, 31)  # time in days
mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]  # substance mass in grams

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the time series data as a scatter plot
ax.scatter(time, mass)

# Label the axes
ax.set_xlabel('Time (days)')
ax.set_ylabel('Mass (grams)')

# Show the plot
plt.show()