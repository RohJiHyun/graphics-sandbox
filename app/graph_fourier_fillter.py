import open3d as o3d
import os.path as osp 
import sys 

filename = __file__
pathp = osp.abspath(__file__)
pathp = osp.dirname(pathp)
pathp = osp.dirname(pathp)
sys.path.append(pathp)

import gmath.laplacian_matrix as lap 
import numpy as np 



mesh  = o3d.io.read_triangle_mesh("./dataset/face5023.obj")
mesh.vertices = o3d.utility.Vector3dVector(np.asarray(mesh.vertices) + np.random.uniform(0, 0.01, size=np.asarray(mesh.vertices).shape))
mesh.compute_vertex_normals()

adj_set = np.asarray(mesh.compute_adjacency_list().adjacency_list)
size = np.asarray(mesh.vertices).shape[0]


w = np.zeros((size, size))
for ridx, i_adj in enumerate(adj_set):
    w[ridx, list(i_adj)] = 1


l = lap.laplacian(w)
print(w)
# print(np.linalg.eig(l)[0])
# print(np.linalg.eig(l)[1])

print(l)
print("original")
o3d.visualization.draw_geometries([mesh])
vv= np.asarray(mesh.vertices)
s = (w)
print(np.diag(l).reshape(-1,1))
t = np.diag(l).reshape(-1,1)
print(s/t)
s = (1000*w/np.diag(l).reshape(-1,1)) @ vv
mesh.vertices = o3d.utility.Vector3dVector(s)
print("mesh adjcency")
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
print("mesh laplacian")
