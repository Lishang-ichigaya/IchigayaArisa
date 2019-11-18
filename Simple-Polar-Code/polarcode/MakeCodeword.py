import numpy as np

def MakeGeneratorMatrix(K):
    G_0 = np.matrix([[1,0], [1,1]])
    G = G_0
    T = K-1
    for i in range(T):
        G = np.kron(G_0,G)
    return G

tttG= MakeGeneratorMatrix(3)
print(tttG)