import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #Data visualisation libraries 
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
# %matplotlib inline

USAhousing = pd.read_csv('USA_Housing.csv')
USAhousing.head()
USAhousing.info()
USAhousing.describe()
USAhousing.columns

# CTC - not working?? 
# sns.pairplot(USAhousing)

x = USAhousing['Price']
y = USAhousing['Avg. Area Number of Rooms']
z = USAhousing['Avg. Area Income']

# X = iris.data[:, :2]  # we only take the first two features.
# y = iris.target

# x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
# y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

x_min, x_max = 0, 10
y_min, y_max = 0, 10

plt.figure(2, figsize=(10, 10))
plt.clf()

# Plot the training points
plt.scatter(x, y, edgecolor='k')
# plt.scatter(x, y, cmap=plt.cm.Set1, edgecolor='k')

plt.xlabel('Price')
plt.ylabel('Area No. of Rooms')

# plt.xlim(x_min, x_max)
# plt.ylim(y_min, y_max)
# plt.xticks(())
# plt.yticks(())

# # To getter a better understanding of interaction of the dimensions
# # plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
# X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(x, y, z, cmap=plt.cm.Set1, edgecolor='k')
ax.set_xlabel("price")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("average area number of rooms")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("average area income")
ax.w_zaxis.set_ticklabels([])

plt.show()