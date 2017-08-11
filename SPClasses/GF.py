class GF:
    def globalfilter(Graph,EV,node):
        if EV ==1:
            S = node.S
        else:
            S = Graph.S[end:1:-1,:]
            
        TrueS = Graph.S[end:1:-1,:]
        Fest    = S*node.GlobalX
        Ftrue   = TrueS*Graph.Xtrue
        I   = mat.eye(Graph.N)
        Theta = mat.zeros((Graph.N,Graph.N))
        D = I
        for i in range(Graph.N-1):
            if Graph.D[i,i]>0.00001:
                filtercoef = 2*(np.square(Fest[0,i])-np.square(Ftrue[0,i]))/(D[i,i]*np.square(Ftrue[0,i]))
                filtercoef  = max(filtercoef,1)
                filtercoef  = min(filtercoef,0)
                Theta[i,i] = filtercoef*D[i,i]
        node.GlobalX = (I - S.T*Theta*S)*node.GlobalX
    ############################
   #############################
    def localadapting(Graph,node):
        I = mat.eye(Graph.N)
        X = mat.zeros((Graph.N,Graph.N))
        for i in range(Graph.N-1):
            e = mat.zeros(Graph.N)
            e[0,i] =1
            node.X[:,i] = node.X[:,i] - Graph.stepsize*np.multiply(node.X[:,i],e) + Graph.stepsize*np.multiply(Graph.Y,e)
    #############################
    def localcombining(Graph,node):
        I = mat.eye(Graph.N)
        Xinter = []
        for i in range(Graph.N-1):
            X = mat.zeros((Graph.N,1)) ## N times 1 column vector 
            for j in range(Graph.N-1):
                X  += Graph.A[i,j]*node.X[:,j]
            if i ==1:
                Xinter = X.copy()
            else:
                 Xinter = np.concatenate(Xinter,X)
        node.X = Xinter.copy()
        #############################
    def localfilter(Graph,EV,node):
        I = mat.eye(Graph.N)
        X = mat.zero((Graph.N,Graph.N))                                                                   
        for i in range(Graph.N-1):
            if EV ==1:
                LocalS = Graph.Local[i].EstS
                D = I                                                           
            else:
                LocalS = Graph.Local[i].S
                D = Graph.Local[i].D                     
            h = mat.zeros((Graph.N,Graph.N))
            LocalFtrue = Graph.Local[i].S*Graph.Local[i].E.T*Graph.Xtrue 
            LocalF = Graph.Local[i].S*Graph.Local[i].E.T*node.X[:,i]
            for j in range(sum(np.int_(LocalFtrue!=0))):
                   htemp =  2*(np.square(LocalF[0,j])-np.square(LocalFtrue[0,j]))/(D[j,j]*np.square(LocalF[0,j]))                                                    
                   htemp = min(htemp,1)
                   htemp = max(htemp,0)                                                          
                   h[0,j] =h_*D[j,j]
            X = node.X[:,i]- Graph.Graph.Local[i].E*LocalS.T*h*LocalS*Graph.Local[i].E.T*node.X[:,i];
        node.X = X.copy()                                                                    
        
        
        
        
        
        