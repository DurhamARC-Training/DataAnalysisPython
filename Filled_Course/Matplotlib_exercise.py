##############
# Exercise 1 # Visualise the points as scatter plots and show the regression line
##############

#
# 1) Loading Data from a JSON file
#

# Load json module
import json

# Create a file open context manager and load dict from JSON
json_path = '../Data/exercise/anscombe.json'
with open(json_path, 'r') as fobj:
    data_dict = json.load(fobj)

# Print the data using the items method of the dict
for key, value in data_dict.items():
    print(key)
    print(value)

#
# 2) Using np.polyfit to generate a linear fit
#

# Import matplotlib and NumPy
import matplotlib.pyplot as plt
import numpy as np

# Get the first dataset, then get its x and y value
dataset = data_dict['dataset1']
x = dataset['x']
y = dataset['y']

# Do the polynomial fit
fit = np.polyfit(x, y, 1)
print(f'for y = mx + b, m={fit[0]}, b={fit[1]}')

# Also get the sum of squared residuals
fit, sum_sq_res, *_ = np.polyfit(x, y, 1, full=True)
print(f'The sum of squared residuals is {sum_sq_res}')

#
# Task for Exercise 1:
# We can use `np.polyfit` for a simple linear regression.
# Use this to visualise and fit Anscombe's quartett.
# (The quartett consists of four datasets that have the same
# mean, variance, correlation, and linear regression line)
# Visualise the points as scatter plots and show the regression line.
# Give labels to the axes and try to vary the colors of the individual components
# of the quartett.
#

# Your solution here
# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
fig2, axs2 = plt.subplots(1, 1, figsize=(8, 1))

for i, ax in enumerate(axs.flat):
    dataset = data_dict[f'dataset{i+1}']
    x = dataset['x']
    y = dataset['y']
    x_fit, residuals, *_ = np.polyfit(x, y, 1, full=True)
    y_fit = np.polyval(x_fit, x)
    ax.plot(x, y_fit, color='red')
    ax.scatter(x, y, color='blue')
    ax.set_title(f'Dataset {i+1}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    axs2.scatter(i, residuals, color='C0')
    # axs2.set_title('Slope of linear fit')
    # axs2.set_xlabel('Dataset')
    # axs2.set_ylabel('Slope')

fig.tight_layout()

# Display the plot
print("Displaying Anscombe's quartett...")
plt.show()

##############
# Exercise 2 # Create your own style
##############

#
# Task 1: Create a mock of graphs from your field
#

# Create data for x1 and y1 using 'np.linspace' and the numpy functions
x1 = np.linspace(0, 4, 10)
y1 = np.exp(-x1)

# Create data for x2 and y2 using 'np.linspace' and the numpy functions
x2 = np.linspace(0, 4, 100)
y2 = np.sqrt(x2)

# Create random data y3a and y3b from x1 using 'np.random.rand'
y3a = x1 * 3 + (np.random.rand(10) - 0.5)
y3b = x1 * 3 + 3 * (np.random.rand(10) - 0.5)

# Create meshgrid xx and yy and data zz
xx, yy = np.meshgrid(np.linspace(0, 2, 100,), np.linspace(0, 2, 100))
zz = np.sin(xx) * np.cos(yy)

# Create figure and axes
fig, axes = plt.subplots(2, 2)

# Plot data y1 on subplot(0,0), y2 on subplot(0,1), y3a and y3b on subplot(1,0), zz on subplot(1,1)
axes[0, 0].plot(x1, y1)
axes[0, 1].hist(y2)
axes[1, 0].scatter(x1, y3a)
axes[1, 0].scatter(x1, y3b)
axes[1, 1].matshow(zz)

# Display the plot
print("Displaying mock graphs...")
plt.show()