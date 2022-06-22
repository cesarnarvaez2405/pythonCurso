# x = 5

# print(x>0 and x<10)

# n = 30

# print(n%2 ==0 or n%3 == 0)


from ctypes.wintypes import PINT


original_str = "The quick brown rhino jumped over the extremely lazy fox"

new_original_str = original_str.split(" ")
num_words_list = []


for n in new_original_str:
    num_words_list.append(len(n))

print(num_words_list)

# num_words_list = len(original_str)