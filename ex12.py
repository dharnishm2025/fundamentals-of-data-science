
# Sample calculation for lower range, upper range and percentile

import numpy as np

array = np.random.randint(1, 100, 16)
array

# Calculate mean
array.mean()

# Calculate percentiles
np.percentile(array, 25)
np.percentile(array, 50)
np.percentile(array, 75)
np.percentile(array, 100)

# Outlier detection
def outDetection(array):
    sorted(array)
    Q1, Q3 = np.percentile(array, [25, 75])
    IQR = Q3 - Q1
    lr = Q1 - (1.5 * IQR)
    ur = Q3 + (1.5 * IQR)
    return lr, ur

lr, ur = outDetection(array)
lr, ur

# Visualize the distribution
import seaborn as sns
sns.displot(array)

# Display distribution (deprecated in newer Seaborn versions)
# sns.distplot(array)

# Remove outliers
new_array = array[(array > lr) & (array < ur)]
new_array

# Visualize the filtered data
sns.displot(new_array)

# Check the new lower and upper ranges
lr1, ur1 = outDetection(new_array)
lr1, ur1
