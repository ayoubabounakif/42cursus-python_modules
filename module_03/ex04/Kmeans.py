import numpy as np
import matplotlib.pyplot as plt
import sys

REGISTERED_AREAS = ['The flying cities of Venus', 'United Nations of Earth', 'Mars Republic', "Asteroids' Belt colonies"]

class KmeansClustering:
    def __init__(self, max_iter=100, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def __calculate_L2_distance(self, matrix, centroids):
        distances = []
        for centroid in centroids:
            distance = []
            for data_point in matrix:
                distance.append(np.sqrt(np.sum((data_point - centroid) ** 2)))
            distances.append(distance)
        distances = np.array(distances)
        return distances

    def __update_centroids(self, matrix, clusters):
        for i in range(self.ncentroid):
            self.centroids[i] = np.mean(matrix[clusters == i], axis=0)

    def __assign_clusters(self, matrix):
        distances = self.__calculate_L2_distance(matrix, self.centroids)
        clusters = np.argmin(distances, axis=0)
        return clusters

    def __generate_random_centroids(self, matrix):
        return matrix[np.random.randint(0, matrix.shape[0], self.ncentroid)]

    def __plot(self, X, y):
        if X.shape[1] == 2:
            plt.scatter(X[:, 0], X[:, 1], c=y)
            plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c='red')
        elif X.shape[1] == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            for label, name in enumerate(REGISTERED_AREAS):
                ax.text3D(X[y == label, 0].mean(),
                        X[y == label, 1].mean() + 1.5,
                        X[y == label, 2].mean(), name,
                        horizontalalignment='center',
                        bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
            ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
            ax.scatter(self.centroids[:, 0], self.centroids[:, 1], self.centroids[:, 2], c='red')
        plt.show()




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
        self.centroids = self.__generate_random_centroids(X)
        for _ in range(self.max_iter):
            clusters = self.__assign_clusters(X)
            self.__update_centroids(X, clusters)
        
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
        return self.__assign_clusters(X)

    def plot(self, X, y):
        if X.shape[1] == 2 or X.shape[1] == 3:
            self.__plot(X, y)
        else:
            print("Cannot plot data with more than 3 dimensions")

def main():
    kmeans = KmeansClustering()
    matrix = np.random.rand(100, 2)
    kmeans.fit(matrix)
    vector = kmeans.predict(matrix)
    kmeans.plot(matrix, vector)

    matrix = np.loadtxt(open(sys.argv[1].split('=')[1], 'rb'), delimiter=',', skiprows=1, usecols=range(1, 4))
    kmeans = KmeansClustering(ncentroid=int(sys.argv[2].split('=')[1]), max_iter=int(sys.argv[3].split('=')[1]))
    kmeans.fit(matrix)
    vector = kmeans.predict(matrix)
    print(kmeans.centroids)
    kmeans.plot(matrix, vector)

if __name__ == "__main__":
    main()