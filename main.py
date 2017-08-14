import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from matplotlib import lines
from numpy import linalg as la
import numpy.matlib as mat
from scipy.spatial.distance  import pdist, squareform# Function to find the Euclidean distance between Node
from NetworkClasses import Network,Local

def main():
    N,L,Slip = synnetwork()
    Graph = Network(N,L)
    Imax = 1000 # Maximum Iteration
    Smax = 1 # Number of Simulation
    Mvar = np.square(5)
    Algnum = 3 # Number of Algorithm 1:LMS 2:GGF,LGF 3:GGF_EV,LGFEV
    node =[]
    msd = []
    Iteration = 1 
    SRun = 1
    msd = []
    for i in range(Alg): # set the initial estimate to zeros of N size.
        node.append(Node(N))
        msd.append(MSD)
    while SRun<Smax:
        Graph.Y = slip + np.sqrt(Mvar)*mat.random.randn((Graph.N,1))
        for a in range(Algnum)
            Alg(Graph,node[a],a)
            if(SRun ==1):
                MSD.g.append(node[a].GLobalMSD)
                MSD.l.append(node[a].LocalMSD)
            else:
                MSD.g[0,Iteration] +=(1/Smax)*node[a].GlobalMSD
                MSD.l[0,Iteration] +=(1/Smax)*node[a].LocalMSD
                
        if(Iteration => Imax):
            Iteration = 1
            SRun += SRun
            del Graph,node
            Graph = Network(N,L)
            for i in range(Alg): # set the initial estimate to zeros of N size.
                node.append(Node(N))
            
        else:
            Iteration += 1
    plotMSD(MSD,Algnum)
        
            
    
if __name__ == '__main__':
    main()
    
    
    
    
#def plottingMSD(MSD,Algnum)
 #   for a in range(Algnum)
  #      hg = 10*np.log10(MSD.g)
  #     hl = 10*np.log10(MSD.l)
     #   plt.plot(hg,)
def Alg(Graph,node,a):
    if(a==0): # Run LMS algorithm
        LMS(Graph,node)
    elif(a==1): # Run EV algorithms (Global and distributed)
        GGF_EV(Graph,node)
        LGF_EV(Graph,node)
    else: # GF algorihtms (Global and distributed)
        GGF(Graph,node)
        LGF(Graph,node)
#########################################    
class MSD:
    g = []
    l = []