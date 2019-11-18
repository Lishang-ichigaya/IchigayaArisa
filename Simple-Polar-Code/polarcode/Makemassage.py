import numpy as np
from numpy.random import randint


class InputMessage:
    def __init__(self, K):
        """
        入力メッセージの生成 (メッセージの長さ)
        """
        self.K = K                                      
        # メッセージのビット数
        self.message = randint(0, 2, np.power(2, K))
        # メッセージ


#tttmessage = InputMessage(5)
#print(tttmessage.message)
