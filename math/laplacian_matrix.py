# make sense!


# geo practice sketch

import numpy as np 

import copy

import math
s = np.array([
        [0, 1, 0, 0, 1, 0],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 0],
       [0, 0, 1, 0, 1, 1],
       [1, 1, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0]])



def laplacian(l):
    """
        l : adj matrix
        return 
            laplacian : L - D - A
    """
    return np.eye(len(l), len(l))*np.sum(l,-1) - l


def norm_lap(l):
    
    """
        l : laplacian matrix

        see https://mathworld.wolfram.com/LaplacianMatrix.html
    """
    size = len(l)
    l = copy.deepcopy(l)
    d = copy.deepcopy(np.diag(l))
    for i in range(size):
        di = d[i]
        for j in range(size):
            if i == j : 
                l[i,j] = 1
            elif l[i,j] != 0:
                l[i,j] = -1/math.sqrt(di*d[j])
    return l


def rescale_lap(l):
    """
        l : normal laplacian

        return 
            rescaled_laplacian. result range [-1, 1]

    """
    m = np.max(np.linalg.eigh(l)[0])
    sl = l*2/m - np.eye(len(l))
    return sl
    

if name == "__main__":
    l =laplacian(s)
    print(s)

    print(f"lap \n{l}")


    # eigenvalue decomposition
    eigenvalues, eigenvectors =  np.linalg.eigh(l)
    print(eigenvalues)
    print(eigenvectors)
    np.set_printoptions(formatter={'float': '{: 0.1f}'.format})

    print((eigenvectors@ np.diag(eigenvalues)@ np.linalg.inv(eigenvectors)))
    print("="*10)

    # normal laplacian
    nl = norm_lap(l)
    print(f"norm lap \n{nl}")
    s = np.random.randn(1,6)
    re = s.dot(nl)
    print(f"re\n{re}")
    print(np.linalg.eigh(nl))

    #rescaled lapacian
    # result values range is [-1, 1]
    m = np.max(np.linalg.eigh(l)[0])
    sl = l*2/m - np.eye(len(l))
    re  = s.dot(sl)
    print(f"{re}")
    print(f"{sl}")






