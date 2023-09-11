import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("musteriler.csv")

X = data.iloc[:,3:].values

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init = "k-means++")
kmeans.fit(X)
print(kmeans.cluster_centers_)

results = []
for i in range(1,10):
    kmeans = KMeans(n_clusters= i, init="k-means++", random_state=42)
    kmeans.fit(X)
    results.append(kmeans.inertia_)

plt.plot(range(1,10), results)
plt.show()

#%%
# hierarchical clustering - agglomerative
from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
Y_tahmin = ac.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=100, c='red', alpha=0.5)
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=100, c='blue', alpha=0.5)
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=100, c='green', alpha=0.5)
plt.scatter(X[Y_tahmin==3,0],X[Y_tahmin==3,1],s=100, c='yellow', alpha=0.5)
plt.title('HC')
plt.show()

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()
