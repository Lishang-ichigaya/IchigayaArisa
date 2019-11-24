from subprocess import check_call
import numpy as np
import sys
from message import Message
from codeword import CodeWorde
from chanel import BSC


if __name__ == '__main__':
    K = 170
    N = 512
    M = int(np.log2(N))
    P = 0.11
    path = "sort_I_" + str(M) + "_" + str(P) + "_" + "20" + ".dat"
    #path ="./polarcode/"+"sort_I_" + str(M) + "_" + str(P) + "_" + "20" + ".dat"

    if len(sys.argv) == 2:
        if sys.argv[1] == "c":
            check_call(["./calIdmcDp.exe", str(M), str(P), "20"])
        else:
            print("相互情報量を計算する場合は 'c' オプションをつける")
            sys.exit()

    if len(sys.argv)==1:
        print("K=", K, "N=", N)

        message = Message(K)
        message.MakeMessage()
        print("メッセージ:\t\t", message.message)

        codeword = CodeWorde(N)
        codeword.MakeCodeworde(K, message.message, path)
        print("符号語:\t\t\t", codeword.codeword)

        bsc011 = BSC(0.11)
        output = bsc011.Transmission(N, codeword.codeword)
        print("通信路出力:\t\t", output)

        estimatedcodeword = CodeWorde(N)
        estimatedcodeword.DecodeOutput(K, N, output, path)
        print("メッセージもどき推定値:\t", estimatedcodeword.codeword)

        estimatedmessage = estimatedcodeword.DecodeMessage(K, path)
        print("メッセージ推定値:\t", estimatedmessage)

        error = np.bitwise_xor(message.message, estimatedmessage)
        print("誤り数:",np.count_nonzero(error))