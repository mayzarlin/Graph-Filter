class alg:
    def LMS(Graph,node):
        node.GlobalX = (1-Graph.stepsize/Graph.N)*node.GlobalX +(Graph.stepsize/Graph.N)*Graph.Y
        node.GlobalMSD = (1/Graph.N)*np.square(la.norm(node.GlobalX-Graph.Xtrue))
############################
    def GGF(Graph,node):
        node.GlobalX = (1-Graph.stepsize/Graph.N)*node.GlobalX +(Graph.stepsize/Graph.N)*Graph.Y
        gf.globalfilter(Graph,0,node)
        node.GlobalMSD = (1/Graph.N)*np.square(la.norm(node.GlobalX-Graph.Xtrue))
 ############################ 
    def LGF(Graph,node):
        gf.localadapting(Graph,node)
        if ACG == 0:
            gf.localcombining(Graph,node)
            gf.localfilter(Graph,0,node)
        else:            
            gf.localfilter(Graph,0,node)
            gf.localcombining(Graph,node)
        if Graph.LGF == 1 
            msd = mat.zeros(Graph.N)
            for i in range(Graph.N-1)
                msd[0,i] = (1/Graph.N)*np.square(la.norm(Graph.Xtrue-node.X[:,i]))
            node.LocalMSD = np.mean(msd)
  ############################ 
    def GGF_EV(Graph,node)
        node.GlobalX = (1-Graph.stepsize/Graph.N)*node.GlobalX +(Graph.stepsize/Graph.N)*Graph.Y
        gf.globalfilter(Graph,1,node)
        node.GlobalMSD = (1/Graph.N)*np.square(la.norm(node.GlobalX-Graph.Xtrue))
        ############################ 
    def LGF(Graph,node):
        gf.localadapting(Graph,node)
        if ACG == 0:
            gf.localcombining(Graph,node)
            gf.localfilter(Graph,0,node)
        else:            
            gf.localfilter(Graph,0,node)
            gf.localcombining(Graph,node)
        if Graph.LGF_EV == 1 
            msd = mat.zeros(Graph.N)
            for i in range(Graph.N-1)
                msd[0,i] = (1/Graph.N)*np.square(la.norm(Graph.Xtrue-node.X[:,i]))
            node.LocalMSD = np.mean(msd)