import numpy.matlib as mat   
class Local:
    L
    S
    EstS
    D
    C
    E
    def __init__(self,N):
        self.L  = mat.zeros((N,N)) #Local Laplacain
        self.S  = mat.zeros((N,N))# Local GFT Matrix
        self.EstS  = mat.zeros((N,N)) # Estimated Local GFT Matrix
        self.D  = mat.zeros((N,N)) # Local Eigenvalue Matrix
        self.C  = mat.zeros((N,N))# Local Covariance Matrix
        self.E  = mat.zeros((N,N))