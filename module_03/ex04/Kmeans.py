import numpy as np
import matplotlib.pyplot as plt
import sys

class KmeansClustering:
    def __init__(self, max_iter=100, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

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
            # Assign each data point to the closest centroid
            distances = []
            for centroid in self.centroids:
                distance = []
                for data_point in X:
                    distance.append(np.sqrt(np.sum((data_point - centroid) ** 2)))
                distances.append(distance)
            distances = np.array(distances)
            self.clusters = np.argmin(distances, axis=0)
            # Update the centroids to be the mean of the points assigned to them.
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
        dist = np.array([np.linalg.norm(X - self.centroids[i], axis=1) for i in range(self.ncentroid)])
        clusters = np.argmin(dist, axis=0)
        return clusters

    def plot(self, X, y):
        if X.shape[1] == 2:
            plt.scatter(X[:, 0], X[:, 1], c=y)
            plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c='red')
        elif X.shape[1] == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
            ax.scatter(self.centroids[:, 0], self.centroids[:, 1], self.centroids[:, 2], c='red')
        plt.show()

if __name__ == "__main__":
    # kmeans = KmeansClustering()
    # matrix = np.random.rand(100, 2)
    # kmeans.fit(matrix)
    # vector = kmeans.predict(matrix)
    # kmeans.plot(matrix, vector)

    matrix = np.loadtxt(open(sys.argv[1].split('=')[1], 'rb'), delimiter=',', skiprows=1, usecols=range(1, 4))
    kmeans = KmeansClustering(ncentroid=int(sys.argv[2].split('=')[1]), max_iter=int(sys.argv[3].split('=')[1]))
    kmeans.fit(matrix)
    vector = kmeans.predict(matrix)
    kmeans.plot(matrix, vector)
