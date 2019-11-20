def func(M):
    if M==1:
        return 1
    return M * func(M-1)

print(func(4))