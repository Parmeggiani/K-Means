import math, random
k = 2
file = open('iris.data.txt')

#   1. sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm

def getTuples():

    tuples = []
    for line in file:
        iris = line.split(',')[0:4]
        tuples.append((float(iris[0]), float(iris[1]), float(iris[2]), float(iris[3])))
    return tuples

def getDistance(tuple_a, tuple_b):
        return float('%.3f' % math.sqrt(sum([(a - b) ** 2 for a, b in zip(tuple_a, tuple_b)])))

def getMean(tuple_a, tuple_b):

    newPoint = []
    for t in zip(tuple_a,tuple_b):
        print(t)
        newPoint.append((t[0]+t[1])/2.0)

    return ((newPoint[0], newPoint[1], newPoint[2], newPoint[3]))


tuple_list = getTuples()
tuples_len = (len(tuple_list)-1)

#Obtér k centróides aleatórios
rand_1 = random.randrange(0, tuples_len)
rand_2 = random.randrange(0, tuples_len)

centroid_1 = tuple_list[0]
centroid_2 = tuple_list[1]
centroid_3 = tuple_list[2]

d1 = getDistance(centroid_1, centroid_3)
d2 = getDistance(centroid_2, centroid_3)
min_d = min(d1, d2)

print("C1: ", centroid_1)
print("C2: ", centroid_2)
print("C3: ", centroid_3)

print("Distance C1-C3: ", d1)
print("Distance C2-C3: ", d2)

mean_tuple = getMean(centroid_1, centroid_3)
print(mean_tuple)