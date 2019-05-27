from numpy import *
import random as rm
import matplotlib.pyplot as plt

#%matplotlib inline

# calculate Euclidean distance


def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))

# init centroids with random samples


def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = dataSet[rm.sample(range(numSamples), k)]
    return centroids

# k-means cluster


def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    clusterAssment = zeros((numSamples, 2))
    clusterChanged = True

    # step 1: init centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        # for each sample
        for i in xrange(numSamples):
            minDist = 100000.0
            minIndex = 0
            # for each centroid
            # step 2: find the centroid who is closest
            for j in range(k):
                distance = euclDistance(centroids[j], dataSet[i])
                if distance < minDist:
                    minDist = distance
                    minIndex = j

            # step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i] = minIndex  # , minDist**2

        # step 4: update centroids
        for j in range(k):
            #pointsInCluster = dataSet[nonzero(clusterAssment[:, 0]== j)[0]]
            pointsInCluster = dataSet[clusterAssment[:, 0] == j]
            centroids[j, :] = mean(pointsInCluster, axis=0)

    print 'Congratulations, cluster complete!'
    return centroids, clusterAssment

# show your cluster only available with 2-D data


def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "dimension 2 please"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "k is too large!"
        return 1

    # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.title('k = %s' % k)
    plt.show()
