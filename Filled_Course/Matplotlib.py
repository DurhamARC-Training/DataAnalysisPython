# Import Matplotlib and NumPy
import matplotlib.pyplot as plt
import numpy as np

###########################
# Using Matplotlib pyplot #
###########################

# Create data for plotting π between 0 and 2*π
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Create a simple plot of a sin function using plt
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

print("Displaying simple sine plot using pyplot...")
plt.show()

#
# Usually I would always use subplots
#

# Create the same plot using figure and axes
fig, ax = plt.subplots()

# Plot the data on the subplots
ax.plot(x, y, color='C2')
ax.set_xlabel(r'$\frac{x}{1}$')
ax.set_ylabel(r'$\sin(x)$')

print("Displaying sine plot using figure and axes...")
plt.show()

#
# If there are multiple plots, using subplots is usually the better idea
#

# Create data for plotting the sin and cos as multiple plots in [0, 2π]
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Plot the data on the subplots
axs[0].plot(x, y1, color='blue', label='sin(x)')
axs[0].scatter(x, y2, color='red', label='cos(x)')
axs[1].plot(x, y2, color='red', label='cos(x)')

# Set titles and labels for each subplot
axs[0].set_title('Sine Function')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')
axs[1].set_title('Cosine Function')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')

# Add legends to the subplots
axs[0].legend()
axs[1].legend()

# Adjust the spacing between subplots
fig.tight_layout()

print("Displaying subplots of sine and cosine functions...")
plt.show()

####################
# Go to Exercise 1 #
####################

#
# Encoding information in plots
#

# Generate random data
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

# Create a figure and subplots
fig, ax = plt.subplots()

# Create a scatter plot, use colour and size for encoding
ax.scatter(
    x, y, c=x * y* 100, marker='o',
    s=x * y* 100,
    alpha=0.5
)

# Set plot title and labels
ax.set_title('Scatter Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Customize plot appearance using grid and legend
ax.grid(True)
ax.legend(['Data Points'])
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

print("Displaying scatter plot with encoded information...")
plt.show()

#
# Plotting categorical data
#

# Load data from a text file
country, gdp = np.loadtxt(
    '../Data/presentation/GDP_G7.csv',
    unpack=True,
    dtype='<U15,float64',
    delimiter=','
)

# Create figure and axes
fig, ax = plt.subplots()

# Create a bar plot
#ax.bar(country, gdp)

# Set xticklabel, including rotation
# ax.set_xticklabels(country, rotation=90)

# Demonstrate horizontal bar plot
ax.barh(country, gdp)
ax.set_xlabel('GDP (in billion USD)')

print("Displaying horizontal bar plot of GDP data...")
plt.show()

#
# If there is no inherent reason to sort data in a certain way, sort by size
#

# Create indexes for sorting the arrays
indexes = np.argsort(gdp)

# Create figure and axes
fig, ax = plt.subplots()

# Create sorted horizontal bar plot
ax.barh(country[indexes], gdp[indexes])
ax.set_xlabel('GDP (in billion USD)')

print("Displaying sorted horizontal bar plot of GDP data...")
plt.show()

#
# We can also set styles using an mplstyle file
#

# Use style for all subsequent plots
plt.style.use('../mpl_styles/colors.mplstyle')
colors = ['C1', 'C1', 'C2', 'C2', 'C3', 'C4', 'C5']

# Create figure and axes
fig, ax = plt.subplots()

# Create the same sorted horizontal bar plot, but with colours
ax.barh(country[indexes], gdp[indexes], color=colors)
ax.set_xlabel('GDP (in billion USD)')

print("Displaying colored horizontal bar plot of GDP data...")
plt.show()

# Or use style within a context
with plt.style.context(('../mpl_styles/presentation.mplstyle')):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'C1-o')
    print("Displaying plot with presentation style...")
    plt.show()

# Apply style to plot
with plt.style.context((
    '../mpl_styles/publication.mplstyle',
    '../mpl_styles/publication_onecolumn.mplstyle')
):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'C2-o')
    print("Displaying plot with one-column publication style...")
    plt.show()

# Apply style to plot
with plt.style.context((
    '../mpl_styles/publication.mplstyle',
    '../mpl_styles/publication_twocolumn.mplstyle'
)):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'C2-o')
    print("Displaying plot with two-column publication style...")
    plt.show()

####################
# Go to Exercise 2 #
####################

#
# Exporting figures
#

# Apply style to plot
with plt.style.context((
    '../mpl_styles/publication.mplstyle',
    '../mpl_styles/publication_twocolumn.mplstyle'
)):
    # Create data
    x = np.linspace(0, 2 * np.pi)

    # Create figure and axes
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(x, np.sin(x), 'C2')
    ax.set_xlabel('$x$')
    ax.set_ylabel(r'$\sin(x)$ / a. u.')

    # Save the plot in a file
    print("Saving figure as 'matplotlib_output.svg'...")
    plt.savefig('matplotlib_output.svg',
                dpi=300,
                bbox_inches='tight',
                format='svg')
    
#########
# Bonus #
#########

#
# Sharing Axes Between Subplots
#

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot data
ax1.plot(x, y1, label='sin(x)')
ax2.plot(x, y2, label='cos(x)')

# Only bottom plot needs x-label
ax2.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax2.set_ylabel('cos(x)')

# Display the plot
print("Displaying subplots with shared x-axis...")
plt.show()

#
# Combining styles
#

# Combine multiple styles
#plt.style.use(['custom_style', 'seaborn-darkgrid'])

# Or in context
#with plt.style.context(['custom_style', 'science']):
    # ...plotting code...

# Print all available styles
print("Available styles:")
print(plt.style.available)

#
# Font Embedding
#

import matplotlib.font_manager as fm

# Ensure fonts are embedded
plt.rcParams['pdf.fonttype'] = 42  # TrueType fonts
plt.rcParams['ps.fonttype'] = 42   # TrueType fonts
plt.rcParams['svg.fonttype'] = 'none'  # For SVG text as text, not paths

# Using specific fonts with fallbacks
plt.rcParams['font.family'] = ['serif']
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']

# For math text
plt.rcParams['mathtext.fontset'] = 'cm'  # Computer Modern for equations

# Check available fonts
print("Available fonts:")
for font in sorted(set([f.name for f in fm.fontManager.ttflist])):
    print(f"- {font}")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
ax.set_title('Plot with Embedded Fonts')
ax.set_xlabel(r'$\alpha$ (radians)')  # Math text example

# Save with font embedding
fig.savefig('plot_with_fonts.pdf',
            metadata={'Creator': 'Matplotlib'},
            bbox_inches='tight',
            dpi=300)
