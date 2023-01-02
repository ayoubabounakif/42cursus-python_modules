import numpy as np
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=50, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

        self.clusters = [] # cluster of each data point

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.

        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
        -------
        None.

        Raises:
        -------
        This function should not raise any Exception.
        """
        # Randomly initialize the centroids (0, X.shape[0], size=self.ncentroid)
        self.centroids = X[np.random.randint(0, X.shape[0], self.ncentroid)]
        for _ in range(self.max_iter):
            # Calculate the distance between each data point in 'X' and each centroid
            # Distance is calculated using the Euclidean distance between two points
            # -> The centroid that is closest to the data point is the cluster that the data point belongs to
            distances = np.array([np.linalg.norm(X - c, axis=1) for c in self.centroids])
            # Assign each data point to the closest centroid
            self.clusters = np.argmin(distances, axis=0)
            print(self.clusters)
            # Update the centroids
            for i in range(self.ncentroid):
                self.centroids[i] = np.mean(X[self.clusters == i], axis=0)
        
    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.

        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.

        Raises:
        -------
        This function should not raise any Exception.
        """
        # f
        # dist = np.array([np.linalg.norm(X - self.centroids[i], axis=1) for i in range(self.ncentroid)])
        # clusters = np.argmin(dist, axis=0)
        # return clusters
        return self.clusters

    def plot(self, X, y):
        plt.scatter(X[:, 0], X[:, 1], c=y)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c='red')
        plt.show()

if __name__ == "__main__":
    kmeans = KmeansClustering()

    matrix = np.random.rand(100, 2)
    kmeans.fit(matrix)
    vector = kmeans.predict(matrix)
    kmeans.plot(matrix, vector)
