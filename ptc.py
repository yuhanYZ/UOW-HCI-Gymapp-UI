#q5:
def Reversal(x): 
    n = str(x)
    res =''
    for ch in n:
        res = ch + res
    return res
if __name__ == '__main__':
    print(Reversal(25))