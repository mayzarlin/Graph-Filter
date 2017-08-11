class GF:
    def globalfilter(Graph,EV,node):
        if EV ==1:
            S = node.S
        else 
            S = Graph.S[end:1:-1,:]
            
        TrueS = Graph.S[end:1:-1,:]
        Fest    = S*node.GlobalX
        Ftrue   = TrueS*Graph.Xtrue
        I   = mat.eye(Graph.N)
        Theta = mat.zeros((Graph.N,Graph.N))
        D = I
        for i in range(Graph.N-1):
            if Graph.D[i,i]>0.00001
                filtercoef = 2*(Fest[i]^2-Ftrue[i]^2