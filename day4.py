#practice the test for day1-day3.
def get_sum():
    nums=[4,7,1,9]
    total = 0
    for i in nums:
        total += i
    return total


def find_greater():
    nums=[4,7,1,9]
    for i in nums:
        if i > 5:
            print(i)

def find_last():
    nums=[4,7,1,9]
    last_index = len(nums) - 1
    return nums[last_index]
def determine_even():
    nums=[3,7,1,9]
    for i in nums:
        if i % 2 == 0:
            return True
    return False
def determine_postive():
    nums = [1, 2, 3, -1]
    for i in nums:
        if i < 0:
            return False
    return True
def find_max():
    nums = [4,7,1,9]
    max=nums[0]
    for i in nums:
        if i > max:
            max = i
    return max
def caculate():
    nums = [1, 2, 1, 3, 2, 1]
    mp={}
    for i in nums:
        mp[i]= mp.get(i,0) + 1
    return mp
def count_alphabet():
    s = 'banana'
    mp={}
    for i in s:
        mp[i]=mp.get(i,0) + 1
    return mp
def get_sum():
    nums = [2, 7, 11, 15]
    target = 9
    mp={}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in mp:
            return (mp[need],i )
        mp[nums[i]]=i
if __name__ =='__main__':
    print(get_sum())