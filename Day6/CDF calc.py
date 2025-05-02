import numpy as np
import matplotlib.pyplot as plt

# Create a sample data set
data=[4, 1, 6, 2, 2, 4, 9, 3, 7, 8, 4]

# Sort the data
data_sorted = np.sort(data)

# Calculate CDF
cdf=np.arange(1, len(data_sorted)+1) / len(data_sorted)
print(cdf)

# Plot CDF
plt.plot(data_sorted, cdf, marker='.', linestyle='none')
plt.xlabel('Value')
plt.ylabel('CDF')
plt.title('CDF of the Data')
plt.grid(True)
plt.show()