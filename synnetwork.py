def synnetwork():
    synColName = ['Latitude','Longitude','Slip'] 
    StationLocation= pd.read_csv('Data/GPS.csv',sep=',',header=None,names = synColName)
    L = np.mat(pd.read_csv('Data/GPSAdjacency.csv',sep=',',header=None))
    Slip = np.mat(StationLocation['Slip'])
    #fig = plt.figure()
    N = len(StationLocation)
    #ax = fig.add_subplot(111)
    plt.plot(StationLocation['Latitude'],StationLocation['Longitude'],'o',alpha = -0.3)
    plt.quiver(StationLocation['Latitude'],StationLocation['Longitude'],Slip,np.zeros(N))
    plt.axhline(0, color='red')
    #ax.annotate('Slip Event', xy=(30,0) , xytext=(38,8) , arrowprops=dict(color='blue', shrink = 1,headwidth=7,width=1),)
    plt.title('Slip Event on Synthetic Network')
    ### Plotting the Edges form Adjacency 
   # plt.show()
    plt.plot(StationLocation['Latitude'],StationLocation['Longitude'],'o',alpha = -0.3)
    for i in range(N):
        for j in range(i+1,N):
            if L[i,j]!=0:
                x = [StationLocation['Latitude'][i],StationLocation['Latitude'][j]]
                y = [StationLocation['Longitude'][i],StationLocation['Longitude'][j]]
                plt.plot(x,y,'g--')
    #plt.subplot(1,2,2)
    #plt.plot(StationLocation['Latitude'],StationLocation['Longitude'],'o',alpha = -0.3)
    plt.title('Network Topology')
 #   plt.show()
    return N,L,Slip