# day5 practice how to use set
# determine wheather there are the repetive digt=its
def determine_repete(nums):
    mp={}
    for i in nums:
        if i in mp:
            return True
        mp[i] = 1
    return False
#learn how to use string 
# Q1:
def PP(s):
    for ch in s:
        print(ch)

#q2:
def reverse(s):
    n =''
    for ch in s:
        n = ch + n
    print(n)
#q3:
def dertermine(s):
    n = ''
    for ch in s:
        n = ch + n
    if n == s:
        return True
    else:
        return False
#q4:
def dd_C(s):
    n=''
    for ch in s:
        n = ch + n
    n =n.lower()
    s =s.lower()
    if n == s:
        return True
    else:
        return False
    
#q5:
def Reversal(x): 
    n = str(x)
    res =''
    for ch in n:
        res = ch + res
    return res

#q6:
def determineR(x):
    n = str(x)
    res =''
    for ch in n:
        res = ch + res
    if int(res) == x:
        return True
    else:
        return False 
#Q7:
def ispalindrome(x):
    x= x.lower()
    left = 0
    right =len(x) - 1
    while left < right:
        if x[left]!=x[right]:
            return False
        else:
            left += 1
            right-= 1
    return True
if __name__ == '__main__':
    print(ispalindrome('right'))