class Network:
    LMS =0
    GGF =0
    LGF =0
    GGF_EV =0
    LGF_EV =0
    setpsize = 0.1
    theta = 0 # TV component
    def __init__(self,N,L):
        self.N       = N
        self.mean = 10*mat.ones((N,1))
        self.L       = L           # Network Laplacian
        self.Y       = mat.zeros((N,1))  # Measurement Data
        self.Xtrue = mat.zeros((N,1))# True Network Data
        ED,EV     = la.eig(L)      # EigenValue and EigenVecotr Matrix of Laplacian. Eigen Value are in Desending Order
        self.D      = np.mat(np.diag(ED))
        self.S       = np.mat(np.transpose(EV)) ## Global GFT matrix
        self.EstS   = mat.random.rand(N,N)# Estimated GFT Matrix
        self.C       = mat.zeros((N,N))# Covariance Matrix
        self.Local  = []
        for i in range(N-1):
            self.Local.append(Local(N))# Contains each node Laplaciand and its eigendecomposition
        NghMat  = np.int_(L!=0)  ## find zeor one Adjacency matrix 
        totalNgh = np.sum(NghMat,axis=1) ## total number of neighbor
        totalNgh = totalNgh.reshape(N,1) ## reshape the total numer of neighbor array
        self.A     = np.mat(diag(1/totalNgh)*NghMat) # weighted adjacency matrix

            ################
    def findLocalL(self):
        for i in range(self.N-1):
            self.Local[i].L[:,i] = 0.5*self.L[:,i]
            self.Local[i].L[i,:] = 0.5*self.L[i,:]
            neighbor = np.nonzero(self.L[i,:])
            for j in range(len(neighbor)-1):
                n = neighbor[0][j]
                self.Local[n,n] = -0.5*self.L[i,n];
            self.Local[i].L[i,i] = 0;
            self.Local[i].L[i,i] = 0.5 + 0.5*sum(self.L[i,:])
            self.LocalEDUpdate
####################
    def LocalEDUpdate(self):
        self.LocalPermulatationMat # find the permutation matrix for each node
        for i in range(self.N-1):
            ngh = sum(np.int_(self.L!=0),axis =1) # numer of node k neighbor
            BigL = self.Local[i].E.T*self.Local[i].L*self.Local[i].E
            SmallL = BigL[1:ngh]
            
####################
    def LocalPermulatationMat(self):
        for i in range(self.N-1):
            k = 2;
            for j in range(self.N-1):
                self.Local[i].E[i,1] = 1 
                if(i!=j & self.Local[i].L[j,j]>0):
                    self.Local[i].E[j,k] = 1;
                    k +=1
####################
    def XtrueUpdate(self):
        self.theta = 0.9*self.theta + math.sqrt(0.01)*self.S.T*la.pinv(self.D)*mat.random.randn(self.N,1) # Update Random Walk in Signal Model
        self.Xtrue = self.mean + self.theta # New Signal at time i
        