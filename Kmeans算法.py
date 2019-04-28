import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
data = [[0.,0],
        [1,0],
        [1,1],
        [4,4],
        [5,4],
        [5,5]]
data = np.array(data)
estimator = KMeans(n_clusters=2)
estimator.fit(data)
label_color = ['r','g']
colors = [label_color[i] for i in estimator.labels_]
centroids = estimator.cluster_centers_
x,y = data.T
xc,yc = centroids.T
plt.scatter(x,y,c=colors)
# 画出聚类中心
plt.scatter(xc,yc,c=['r','g'],s = 100, marker= 'X')
plt.axis()
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()