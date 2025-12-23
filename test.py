'''
Docstring for test
🟢 Part A：Day 1（数组 list）
题 1️⃣

给你一个数组：

nums = [3, 5, 7, 9]


👉 问题：
打印所有数字的和。
'''

def get_sum():
    nums =[3, 5, 7, 9]
    total = 0
    for i in nums:
        total += i
    return total

'''
🟢 Part B：Day 2（if + return）
题 3️⃣

写一个函数，判断数组里 是否存在负数：


👉 要求：

找到一个就可以结束

返回 True / False
'''
def find_nagative():
    nums = [1, 3, -2, 5]
    for i in nums:
        if i < 0:
            return True
    return False
if __name__=='__main__':
    print(find_nagative())

