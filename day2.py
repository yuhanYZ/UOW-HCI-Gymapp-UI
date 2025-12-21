#三、例子 1：只打印偶数（入门必做）
def printEven():
    nums =[1,2,3,4,5,6,7,8]
    for i in nums:
        if i % 2 ==0:
            print(i)
#例子 2：统计数量（非常重要）

def counts_postive():
    nums=[1,2,-1,-3,4,8,-6,9,5]
    counts=0
    for x in nums:
        if x > 0:
            counts += 1
    print(counts)
#例子 3：求最大值（经典）
def find_max():
    nums=[1,2,5,8,10,25,36,24]
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
        return max_num
    print()

def greater():
    for i in nums:
        if i > 3:
            print(i)
def IsEven(nums):
    counts= 0
    for i in nums:
        if i % 2 ==0:
            counts += 1
            return counts
    
def find_least(nums):
    min_num=nums[0]
    for i in nums:
        if i <min_num:
            min_num = i
            return min_num
    

if __name__ == '__main__':
    nums=[1,2,5,8,10,25,36,24]
    print(IsEven(nums))