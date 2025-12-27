    #statistical the number
def statistical_num(nums):
    mp= {}
    for i in nums:
        mp[i] =mp.get(i,0) +1
    return mp

def statistical_letter(s):
    mp={}
    for ch in s:
            mp[ch]=mp.get(ch,0) +1
    return mp

#contain duplicate
def determine_duplicate(nums):
    mp={}
    for i in nums:
        if i in mp:
            return True
        mp[i] = 1
    return False
# isomorphic string
def determine_isomorphic(s1,s2):
     if len(s1) != len(s2):
        return False
     mp1 = {}
     mp2 = {}
     # s1='add',s2 ='egg'
     for i in range(len(s1)):
        char_s1 =s1[i]
        char_s2 =s2[i]
        if char_s1 not in mp1:
             mp1[char_s1] = char_s2
        else:
             if mp1[char_s1] != char_s2:
                  return False
        if char_s2 not in mp2:
             mp2[char_s2] = char_s1
        else:
             if mp2[char_s2] != char_s1:
                  return False
     return True


def determine_duplicate(s):
     mp={}
     for ch in s:
          if ch in mp:
               return True
          mp[ch] = 1
     return False

if __name__ =='__main__':
     print(determine_isomorphic('add','egg'))