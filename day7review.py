# log_data = "2024-05-12,SUCCESS,Login_User;2024-05-12,FAIL,Search_Action;2024-05-13,SUCCESS,Logout_User"
# # Split the log data into individual entries
# log_entries = log_data.split(';')
# print(f'after split by ;, The log change to{log_entries}')
# record = []
# for entry in log_entries:
#     element = entry.split(',')
#     # 在这里将 list 转换为 tuple
#     record.append(tuple(element)) 

# # 最终 record 就是 [('date', 'status', 'action'), ...]
# print(f"Final records list: {record}")


# #second practice 将字符串转换为单词列表，并统一转换为小写（防止 Python 和 python 被当成两个词）。
# text = "Python is great and python is easy to learn"
# new_text = text.lower()
# word_info =[]
# new_text = new_text.split()
# print(new_text)
# for word in new_text:
#     item=(word,len(word))
#     word_info.append(item)
# print(word_info)


#practice 3 '''    slicing ''''   ' .join '

phones = ["13812345678", "13988887777", "13700001111"]
masked_phones =[]
for num in phones:
    masked_num = num[:3]+'****'+num[7:]
    masked_phones.append(masked_num)
result = ','.join(masked_phones)
print(result)