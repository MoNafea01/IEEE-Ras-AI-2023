"""
Use broadcasting to create a 4 x 4 ndarray that has its first column full
of ones, its second column full of twos, its third column full of threes, etc..
""""

print(np.ones(shape=(4,4),dtype=int) * np.arange(1,5))
