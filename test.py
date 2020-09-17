import numpy as np

initialVector = [24,39, 3,63, 7,46,16, 3,
				 12,57,18,46,12,55,35,43,
				 15, 6,25,53, 0,45,60,15,
				 50,22,37,41,62,56,29,38,
				  9,15,60, 2,55, 3,18, 8,
				 54,10,28, 0,61,40,14,41,
				 12, 2,40,27,23,43,36,62,
				 32,60,45, 4,17,11,21, 4]

permutations=np.genfromtxt("permutation.csv",delimiter=",",dtype=np.uint8)

combinations=np.genfromtxt("combination.csv",delimiter=",",dtype=np.uint8)




#permutation and also for verification of integrity
temp = initialVector[:]
tempshadow = initialVector[:]
for temp1 in range(64):
    for temp2 in range(64):
        tempshadow[temp2] = temp[permutations[temp1][temp2]]
    temp = tempshadow[:]

print(temp)