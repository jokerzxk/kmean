from numpy import *
from PIL import Image
import random
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111, projection='3d')


def loaddata():
    img = Image.open("image2.jpg")
    img_array = img.load()
    photoX, photoY = img.size

    X = zeros((photoX * photoY, 3), dtype=int)
    for i in range(0, photoX):
        for j in range(0, photoY):
            index = i * photoY + j
            X[index] = img_array[i, j]

    print type(img_array), img.size, type(img_array[10, 10])

    # ax.scatter(X[:,0], X[:,1], X[:,2])
    #	img.show()
    return X, img


def randominit(K, phsize, X):
    iniCluster = zeros((K, 3), dtype=int)
    for i in range(0, K):
        c = random.randint(0, phsize[0] * phsize[1] - 1)
        iniCluster[i] = X[c]
    return iniCluster


def FindMinCluster(Cluster, phsize, X, K):
    indexcluster = zeros(phsize[0] * phsize[1])
    for i in range(0, phsize[0] * phsize[1]):
        mindis = sum(power(X[i] - Cluster[0], 2))
        indexcluster[i] = 0
        da = tile(X[i], (K, 1))
        dis = sum(power(da - Cluster, 2), 1)
        re = where(dis == dis.min(0))
        indexcluster[i] = re[0][0]

    return indexcluster


def MoveCluster(X, K, indexcluster, phsize):
    Cluster = zeros((K, 3), dtype=int)
    for i in range(0, K):
        dada = X[indexcluster == i, :]
        sdada = sum(dada, 0)
        Cluster[i] = sdada / dada.shape[0]
    return Cluster


if __name__ == '__main__':
    [X, img] = loaddata()
    K = 16
    phsize = img.size
    iniCluster = randominit(K, phsize, X)

    for i in range(0, 10):
        indexcluster = FindMinCluster(iniCluster, phsize, X, K)
        iniCluster = MoveCluster(X, K, indexcluster, phsize)
        print iniCluster
        ax.scatter(iniCluster[:, 0], iniCluster[:, 1], iniCluster[:, 2], color='red')

    # plt.show()

    for i in range(0, phsize[0]):
        for j in range(0, phsize[1]):
            index = i * phsize[1] + j
            [a, b, c] = iniCluster[indexcluster[index]]
            img.putpixel((i, j), (a, b, c))

    img.show()
    img.save('imag.jpg')



