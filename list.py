# creat a list
def practice():
    nums=[1,2,3]
    print(f'{nums[0]}\n{nums[1]}')
    print(nums[2])
    #add one more element in this list
    nums.append(4)
    print(nums)

    for i in nums:
        print(i)
def practice_2():
    'create and get the number'
    num=[1,2,3,4,5,6]
    print(num[0])
    print(num[5])
#练习 2：遍历
# nums = [3, 5, 7]
# 用 for 循环打印每个数字
def practice_3():
    a = [3,5,7]
    for i in a:
        print(i)
        '''
练习 3：求和（非常重要）
nums = [1, 2, 3, 4]

total = 0
# 用 for 循环，把 nums 里的数加到 total
print(total)   # 结果应该是 10


这一步 = 所有算法题的祖宗
        '''
def practice_4():
    nums = [1, 2, 3, 4]
    total = 0
    for i in nums:
        total =total + i
    print(total)
if __name__ == '__main__':
    practice_4()