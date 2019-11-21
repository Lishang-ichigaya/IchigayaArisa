import numpy as np


def GetGeneratorMatrix(N):
    """
    ポーラ符号の生成行列を作成
    M: 符号長N
    """
    M = int(np.log2(N))

    matrixF = np.array([[1, 0], [1, 1]], dtype=np.uint8)

    matrixG = matrixF
    for i in range(1, M):
        tmp = matrixG
        matrixG = np.dot(
            GetPermutationMatrix(i+1),
            np.kron(matrixF, tmp)
        )
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
    if M == 1:
        return np.identity(1, dtype=np.uint8)
    matrixI_2 = np.matrix([[1, 0], [0, 1]])
    matrixR = np.matrix([[1, 0], [0, 1]])
    for i in range(M-1):
        matrixR = np.kron(matrixI_2, matrixR)
    matrixEven, matrixOdd = matrixR[::2], matrixR[1::2]
    matrixR = np.concatenate([matrixEven, matrixOdd]).T
    return matrixR


def GetInformationIndex(K, path="sort_I_0.11.dat"):
    """
    情報ビットに対応するインデックス集合を得る
    K:メッセージの長さ
    """
    informationindex = np.loadtxt(path, dtype=np.uint8)
    # 相互情報量orバタチャリアパラメータ順に、インデックスを並べ替えたものを外部で用意しておく
    # print(informationindex[:K])
    return np.sort(informationindex[:K])


class CodeWorde:
    def __init__(self, N):
        """
        符号語の初期化
        N:符号長
        """
        self.N = N
        # メッセージのビット数
        self.codeword = np.zeros(N, dtype=np.uint8)

    def MakeCodeworde(self, K, message, informationindex):
        j = 0
        for i in range(self.N):
            if i == informationindex[j]:
                self.codeword[i] = message[j]
                j += 1
                if j > K-1:
                    j = K-1
            else:
                self.codeword[i] = 0
        # print("生成行列にかけるもの：")
        # print(self.codeword)
        self.codeword = np.dot(self.codeword, GetGeneratorMatrix(self.N)) % 2

    def DecodeOutput(self, N, chaneloutput):
        estimatedcodeword = np.array([], dtype=np.uint8)
        for i in range(N):
            hat_ui = self.EstimateCodeword_ibit(N, chaneloutput, i, estimatedcodeword)
            estimatedcodeword = np.insert(estimatedcodeword, i, hat_ui)
        return estimatedcodeword

    def EstimateCodeword_ibit(self, N, chaneloutput, i, estimatedcodeword):
        L = self.CalculateLR(N, chaneloutput, i, estimatedcodeword)
        return 0 if L>=1 else 1
    
    def CalculateLR(self, N, chaneloutput_y, i, estimatedcodeword_u):
        y_1 = chaneloutput_y[:int(N/2)]
        y_2 = chaneloutput_y[int(N/2):]
        return 1.9

# tt = GetGeneratorMatrix(3)
# print(tt)
# ttt = CodeWorde(16)
# print(ttt.codeword)
"""
KKK=4
NNN=8
message=np.array([0,1,1,0], dtype = np.uint8)
print("メッセージ：", end = "")
print(message)

abv=GetInformationIndex(KKK)
print("情報ビットの位置：", end = "")
print(abv)

print("生成行列：")
print(GetGeneratorMatrix(NNN))

# print("並べ替え行列")
# print(GetPermutationMatrix(3))

testcodeword=CodeWorde(NNN)

testcodeword.MakeCodeworde(KKK, message, GetInformationIndex(KKK))

print("符号語：")
print(testcodeword.codeword)


#ttt = GetGeneratorMatrix(8)
# print(ttt)
"""


N=8
message = np.array([0,0,1,0,1,0,0,0])
test = CodeWorde(N)
estimated =  test.DecodeOutput(N, message)

print(message)
print(estimated)
