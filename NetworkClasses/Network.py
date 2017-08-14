import numpy as np
from numpy import linalg as la
from NetworkClasses import Local as Local
import numpy.matlib as mat   
class Network:
    LMS =0
    GGF =0
    LGF =0
    GGFEV =0
    LGFEV =0
    ACG  = 0 # 0 : ACG, 1:AGC
    setpsize = 1
    theta = 0 # TV component
    def __init__(self,N,L):
        self.N       = N
        self.Xmean = 10*np.ones((N,1))
        self.L       = L           # Network Laplacian
        self.Y       = mat.zeros((N,1))  # Measurement Data
        self.Xtrue = mat.zeros((N,1))# True Network Data
        ED,EV     = la.eig(L)      # EigenValue and EigenVecotr Matrix of Laplacian. Eigen Value are in Desending Order
        self.D      = np.mat(np.diagflat(ED))
        self.S       = np.mat(np.transpose(EV)) ## Global GFT matrix
        self.EstS   = np.mat(mat.random.rand(N,N)) # Estimated GFT Matrix
        self.C       = mat.zeros((N,N))# Covariance Matrix
        self.Local  = []
        for i in range(N):
            self.Local.append(Local(N))# Contains each node Laplaciand and its eigendecomposition
        NghMat  = np.int_(L!=0)  ## find zeor one Adjacency matrix 
        totalNgh = np.sum(NghMat,axis=1) ## total number of neighbor
        totalNgh = totalNgh.reshape(N,1) ## reshape the total numer of neighbor array
        self.A     = np.mat(np.diagflat(1/totalNgh)*NghMat) # weighted adjacency matrix
        self.findlocalL

            ################
    def findlocalL(self):
        for i in range(self.N):
            self.Local[i].L[:,i] = 0.5*self.L[:,i]
            self.Local[i].L[i,:] = 0.5*self.L[i,:]
            neighbor = np.nonzero(self.L[i,:])
            for j in range(len(neighbor)-1):
                n = neighbor[0][j]
                self.Local[n,n] = -0.5*self.L[i,n];
            self.Local[i].L[i,i] = 0;
            self.Local[i].L[i,i] = 0.5 + 0.5*sum(self.L[i,:])
            self.localpermutationM
            self.LocalEDUpdate
####################
    def localEDupdate(self):
        self.LocalPermulatationMat # find the permutation matrix for each node
        for i in range(self.N):
            ngh = sum(np.int_(self.L!=0),axis =1) # numer of node k neighbor
            BigL = self.Local[i].E.T*self.Local[i].L*self.Local[i].E #Permute the local laplacian
            SmallL = BigL[0:ngh-1,0:ngh-1]  # Extract small local laplacian 
            LED,LEV = la.eig(SmallL) # eigen decomposition of small local laplacian
            self.Local[i].D[0:ngh-1,0:ngh-1] = np.diagflat(LED)# update the eigen value matrix of local laplacian
            self.Local[i].S[0:ngh-1,0:ngh-1] = LEV.T # update the eigenvector matrix of local laplacian
            
####################
    def localpermutationM(self):
        for i in range(self.N):
            k = 2;
            for j in range(self.N):
                self.Local[i].E[i,1] = 1 
                if(i!=j & self.Local[i].L[j,j]>0):
                    self.Local[i].E[j,k] = 1;
                    k +=1
####################
    def Xtrueupdate(self):
        self.theta = 0.9*self.theta + math.sqrt(0.01)*self.S.T*la.pinv(self.D)*mat.random.randn(self.N,1) # Update Random Walk in Signal Model
        self.Xtrue = self.Xmean + self.theta # New Signal at time i
####################
    def globalCupdateandestimate(self):
        I = mat.eye(self.N)
        self.C = self.C + (self.Y*self.Y.T) # update global covariance matrix 
        V = self.EVtracking(self.S.T,self.C+I) # update eigenvector matrix
        self.S = V.T
#################### 
    def localCupdateandestimate(self):
        for i in range(self.N):
            nghList = np.int_(self.L!=0)
            NeighborY = slef.Local[i].E.T*np.multiply(nghList.T,self.Y) # get neighbor measurement data
            self.Local[i].C += NeighborY*NeighborY.T # Update the Local Covariance matrix 
            SmallC = self.C[0:sum(nghList)-1,0:sum(nghList)-1] + mat.eye(sum(nghList)) # extract small size covariance matrix
            SmallV = self.Local[i].EstS[0:sum(nghList)-1,0:sum(nghList)-1] .T # extract small eigenvectror matrix 
            SmallV = self.EVtracking(SmallV,SmallC)  # update the eigenvector matrix
            self.Local[i].EstS[0:sum(nghList)-1,0:sum(nghList)-1] = SmallV.T # save in big matirx
####################    
    def EVtracking(V,L):
        n = len(V)
        UpdateV = mat.zeros((n,n))
        ss = 1/la.norm(L)
        I  = mat.eye(n)
        for i in range(N):
                W = mat.zeros((n,n))
                for j in range(0,i):
                    W += V[:,j]*V[:,j].T
                UpdateV[:,i] = V[:,i] + ss*(I -V[:,i]*V[:,i].T)*L*(I-W)*V[:,i]
                UpdateV[:,i] = UpdateV[:,i]/la.norm(UpdateV[:,i])
        return UpdatV
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    