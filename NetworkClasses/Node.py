import numpy.matlib as mat
class Node:
    GlobalMSD = 0
    LocalMSD = 0
    def __init__(self,N):
        self.GlobalX = mat.zeros((N,1)) # Global Estimate
        self.X = mat.zeros((N,N)) # Each column corresponds to each node Estimate 