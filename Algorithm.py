def LMS(Graph,node):
    if(Graph.LMS==1)
        GF.globaladapting(Graph,node)
        node.GlobalMSD = (1/Graph.N)*np.square(la.norm(Graph.Xtrue - node.GlobalX))
def GGF(Graph,node):
    if(Graph.GGF ==1):
        GF.globaladapting(Graph,node)
        GF.globalfilter(Graph,0,node)
        node.GlobalMSD = (1/Graph.N)*np.square(la.norm(Graph.Xtrue - node.GlobalX))
def LGF(Graph,node):
    if(Grpah.LGF == 1):
        GF.localadapting(Graph,node)
        if(ACG ==0):
            GF.localcombining(Graph,node)
            GF.localfilter(Graph,0,node)
        else:
            GF.localfilter(Graph,0,node)
            GF.localcombining(Graph,node)
        errorsquared = []
        for i in range(Graph.N):
            errorsquared.append((1/Graph.N)*np.square(la.norm(Graph.Xtrue - node.X[:,i])))
        node.LOcalMSD = np.mean(errorsquared)
def GGF_EV(Graph,node):
    if(Grpah.LGFEV == 1):
        GF.localadapting(Graph,node)
        if(ACG ==0):
            GF.localcombining(Graph,node)
            GF.localfilter(Graph,1,node)
        else:
            GF.localfilter(Graph,1,node)
            GF.localcombining(Graph,node)
        errorsquared = []
        for i in range(Graph.N):
            errorsquared.append((1/Graph.N)*np.square(la.norm(Graph.Xtrue - node.X[:,i])))
        node.LOcalMSD = np.mean(errorsquared)
def LGF_EV(Graph,node):
    if(Graph.GGFEV ==1):
        GF.globaladapting(Graph,node)
        GF.globalfilter(Graph,1,node)
        node.GlobalMSD = (1/Graph.N)*np.square(la.norm(Graph.Xtrue - node.GlobalX))