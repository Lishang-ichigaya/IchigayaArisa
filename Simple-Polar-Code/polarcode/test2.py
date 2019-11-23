import numpy as np
from decimal import Decimal


def CalculateLR(N, chaneloutput_y, i, estimatedcodeword_u):
    """
    尤度比LRを計算する
    N:符号長
    chaneloutpuy_y:受信したビット列
    i:推定したいビット位置
    estimatedcodeword_u:現在までに推定された符号語ビット列
    """
    if N == 1:
        return Decimal(0.11/0.89) if chaneloutput_y == np.array([1]) else Decimal(0.89/0.11)

    #print("N = ", N, ", i = ", i)

    y_1 = chaneloutput_y[:int(N/2)]
    y_2 = chaneloutput_y[int(N/2):]

    if i > 1:
        # ここからuが存在するときの？
        hat_u_i = estimatedcodeword_u[i-1]

        j = i if i % 2 == 0 else i-1
        # ⇔ j-1 = i-1 or i-2
        estimatedcodeword_u = estimatedcodeword_u[:j]

        # 偶数と奇数に分解
        hat_u1 = estimatedcodeword_u[::2]
        hat_u2 = estimatedcodeword_u[1::2]

        # 偶奇でxor、奇数はそのまま
        #hat_u1 = np.bitwise_xor(hat_u1, hat_u2) if j > 0 else np.array([], dtype=np.uint8)
        hat_u1 = hat_u1 ^ hat_u2
        hat_u2 = hat_u2
        # ここまで
    else:
        # uが存在しないときのそうさ
        # ⇔ i<=1
        if i == 1:
            hat_u_i = estimatedcodeword_u[0]

        j = 0
        hat_u1 = np.array([], dtype=np.uint8)
        hat_u2 = np.array([], dtype=np.uint8)

    # print(hat_u1)
    # print(hat_u2)

    if i % 2 == 0:
        LR1 = CalculateLR(int(N/2), y_1, int(j/2), hat_u1)
        LR2 = CalculateLR(int(N/2), y_2, int(j/2), hat_u2)
        #print("e, ","N = ", N, ", i = ", i,LR1 ,", ", LR2)
        LR = (
            (LR1 * LR2 + 1)
            /
            (LR1 + LR2)
        )
        # LR = 3
    else:
        """
        LR = (
            np.power(CalculateLR(int(N/2), y_1, int(j/2), hat_u1), (1 - 2 * hat_u_i))
            *
            CalculateLR(int(N/2), y_2, int(j/2), hat_u2)
        )"""
        LR1 = CalculateLR(int(N/2), y_1, int(j/2), hat_u1)
        LR2 = CalculateLR(int(N/2), y_2, int(j/2), hat_u2)
        #print("o, ","N = ", N, ", i = ", i,LR1 ,", ", LR2)
        if hat_u_i == 0:
            LR = LR1 * LR2
        else:
            LR = np.reciprocal(LR1) * LR2
        # LR=0.2
    return LR

"""
N = 8
output = np.array([0,0,1,0,0,0,0,0], dtype=np.uint8)
i = 0
hat_u = np.array([], dtype=np.uint8)

print("受信系列:\t\t", output)
print("i-i番目までの復号系列:\t", hat_u)
LR = CalculateLR(N, output, i, hat_u)
print("LR: " ,LR)
print("u_",i," = ", 0 if LR>=1 else 1)
"""
"""
        test1 = np.array([1,0,0,1])
        test2 = np.array([1,0,1,0])

        test3 = np.bitwise_xor(test1,test2)
        print(test1)
        print(test2)
        print(test3)
"""
