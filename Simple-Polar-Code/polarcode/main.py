from message import Message
from codeword import CodeWorde
from chanel import BSC


K=10
N=32
print("K=",K,"N=",N)

message = Message(K)
message.MakeMessage()
print("メッセージ:",message.message)

codeword = CodeWorde(32)
codeword.MakeCodeworde(K,message.message,"sort_I_5_0.11_20.dat")
#codeword.MakeCodeworde(K,message.message,"./polarcode/sort_I_5_0.11_20.dat")
print("符号語:", codeword.codeword)
print(type(codeword.codeword))
print(type(message.message))

bsc011 = BSC()
output = bsc011.Transmission(N,codeword.codeword)
print("通信路出力:", output) 