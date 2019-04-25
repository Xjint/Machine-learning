from scipy.cluster import hierarchy
from scipy import  cluster
import matplotlib.pyplot as plt
X = [[0,0],
     [0,1],
     [2,0],
     [3,3],
     [4,4]]
Z = hierarchy.linkage(X,'single')
cutree = cluster.hierarchy.cut_tree(Z,height= 1.6)
print(cutree)
dn = hierarchy.dendrogram(Z)
plt.show()
