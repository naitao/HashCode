'''
def Fib(max):
    count, F0, F1 = 0, 0, 1
    L = []
    L.append(F0)
    L.append(F1)
    while count < max-2:
        F2 = F0 + F1
        L.append(F2)
        F0, F1 = F1, F2
        count += 1
    return L
'''

def Fib(max):
    count, F0, F1 = 0, 0, 1
    while count < max:
        yield F0
        F2 = F0 + F1
        F0, F1 = F1, F2
        count += 1

for num in Fib(8):
    print(num, "", end="")
