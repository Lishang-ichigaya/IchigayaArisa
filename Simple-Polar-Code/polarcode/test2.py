import numpy as np


def CalculateLR(N, chaneloutput_y, i, estimatedcodeword_u):
        if N==1:
            return 3 if chaneloutput_y==1 else 0.2
        y_1 = chaneloutput_y[:int(N/2)]
        y_2 = chaneloutput_y[int(N/2):]

        hat_u_i = estimatedcodeword_u[i]

        j = i if i % 2 == 1 else i-1
        estimatedcodeword_u = estimatedcodeword_u[:j+1]
        # 偶数と奇数に分解
        hat_u1 = estimatedcodeword_u[::2]
        hat_u2 = estimatedcodeword_u[1::2]
        print(hat_u1)
        print(hat_u2)
        # 偶奇でxor、奇数はそのまま
        hat_u1 = np.bitwise_xor(hat_u1, hat_u2)
        hat_u2 = hat_u2

        if i % 2 == 1:
            LR = (
                (CalculateLR(int(N/2), y_1, int(j/2), hat_u1) * CalculateLR(int(N/2), y_2, int(j/2), hat_u2) + 1)
                    /
                (CalculateLR(int(N/2), y_1, int(j/2), hat_u1) + CalculateLR(int(N/2), y_2, int(j/2), hat_u2))
                )
            # LR = 3
        else:
            LR=(
                (CalculateLR(int(N/2), y_1, int(j/2), hat_u1)) ^ (1 - hat_u_i) 
                    * 
                CalculateLR(int(N/2), y_2, int(j/2), hat_u2)
                )
             #LR=0.2
        return LR


N=8
output=np.array([0, 0, 1, 0, 1, 0, 0, 0])
i=6
hat_u=np.array([0, 0, 1, 0, 1, 0, 0], dtype=np.uint8)


LR=CalculateLR(N, output, i, hat_u)
print(LR)


"""
        test1 = np.array([1,0,0,1])
        test2 = np.array([1,0,1,0])

        test3 = np.bitwise_xor(test1,test2)
        print(test1)
        print(test2)
        print(test3)
"""
