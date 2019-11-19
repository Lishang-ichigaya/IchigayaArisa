import numpy as np


def GetGeneratorMatrix(M):
    """
    ポーラ符号の生成行列を作成 
    M: 符号長Nについて、N=2^Mを満たすM
    """
    matrixF_2 =np.matrix([[1,0],[1,1]])
    matrixF = np.matrix([[1,0], [1,1]])
    matrixB = GetPermutationMatrix(M)
    for i in range(M-1):
        matrixF = np.kron(matrixF_2, matrixF)
    matrixG = np.dot(matrixB, matrixF)
    return matrixG


def GetPermutationMatrix(M):
    """
    偶数番目を前に、奇数番目を後ろに置き換える行列を得る
    M: 符号長Nについて、N=2^Mを満たすM

    例:
    [1,0,0,0]  [1,0,0,0]
    [0,1,0,0]->[0,0,1,0]
    [0,0,1,0]  [0,1,0,0]
    [0,0,0,1]  [0,0,0,1]
    """
    matrixI_2 = np.matrix([[1, 0], [0, 1]])
    matrixB = np.matrix([[1, 0], [0, 1]])
    for i in range(M-1):
        matrixB = np.kron(matrixI_2, matrixB)
    matrixEven, matrixOdd = matrixB[::2], matrixB[1::2]
    matrixB = np.concatenate([matrixEven, matrixOdd]).T
    return matrixB

class CodeWorde:
    def __init__(self, N):
        """
        符号語の初期化 
        N:符号長
        """
        self.N =N                                      
        # メッセージのビット数
        self.codeword = np.zeros(N)        

#tt = GetGeneratorMatrix(3)
#print(tt)
#ttt = CodeWorde(16)
#print(ttt.codeword)