import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from voronoi import voronoi 



# points in R^2
pins = np.random.rand(100,2)

# boundary points in R^2
bnd = np.random.rand(30,2)

# create the polytope bounded voronoi diagram
pnts,vorn = voronoi(pins,bnd)


# plot the result...
pntsv = [ [] for row in pnts]
plt.plot(pnts[:,0],pnts[:,1],'o')

for i, obj in enumerate(pnts):
	pntsv[i] =  np.array(vorn[i])
	if len(pntsv[i]) >= 3:
		vorhull = ConvexHull(pntsv[i])		
		plt.plot(pntsv[i][:,0],pntsv[i][:,1],'x')
		for simplex in vorhull.simplices:
			plt.plot(pntsv[i][simplex, 0],pntsv[i][simplex,1],'k-')
plt.axis('equal')
plt.show()

