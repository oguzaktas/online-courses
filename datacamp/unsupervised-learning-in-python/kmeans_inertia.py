'''
Instructions
- For each of the given values of k, perform the following steps:
- Create a KMeans instance called model with k clusters.
- Fit the model to the grain data samples.
- Append the value of the inertia_ attribute of model to the list inertias.
- The code to plot ks vs inertias has been written for you, so hit 'Submit Answer' to see the plot!
'''

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    model.fit(samples)
    
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
