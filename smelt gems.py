# The player uses fire to smelt gems. After each smelting, there is a chance to upgrade the fire. The higher the level of the fire, the better the gems that can be smelted.
# The level L, the number of smeltings N, and the guaranteed slot M. When M=30, the guarantee is triggered and L is directly assigned a value of 5.
# The probability of upgrading each time is 0.4. When L=5, the fire will return to level 1 directly after smelting.
# When L=5 and M=30, the guarantee is triggered to directly upgrade to level 5, instead of returning to level 1.

import random
L = 1
M = 0
N = 0

# Store the results of L in a list
list = []

# Get the occurrence of each element in the list
def all_list(arr):
  result = {}
  for i in set(arr):
    result[i] = arr.count(i)
  return result

# The smelting process starts
while N < 10000:
    if M >= 30:   # When M >= 30, the guarantee is triggered and directly upgraded to level 5 while clearing the guaranteed slot
        L = 5
        M = 0
    else:
        if L == 5:   # When L = 5, it fails, and the guaranteed slot accumulates 5
            L = 1
            M = M + 5
        else:
            p = random.random()
            # Successful strengthening, level +1, and guaranteed slot increases
            if p < 0.4:
                M = M + L
                L = L + 1
            # Failed strengthening, directly return to level 1, and guaranteed slot increases
            else:
                M = M + L
                L = 1
    N = N + 1

    # Store the level L in a list
    list.append(L)
    # Get the occurrence of each element in the list
    a = all_list(list)
print(a)

# import random
# L = 1
# M = 0
# N = 0
#
# #储存L的结果
# list = []
#
# # 获取所有元素的出现次数
# def all_list(arr):
#   result = {}
#   for i in set(arr):
#     result[i] = arr.count(i)
#   return result
#
# # 熔炼开始
#
# while N<10000:
#     if M>= 30:   #M>=30  触发保底,直升5，同时清空保底槽。
#         L = 5
#         M = 0
#     else:
#         if L==5:   #L=5时，必然失败，保底槽积累5
#             L = 1
#             M = M+5
#         else:
#             p = random.random()
#             # 强化成功，等级+1，保底槽也增加
#             if p < 0.4:
#                 M = M + L
#                 L = L+1
#             # 强化失败，直接回到1级，保底槽增加
#             else:
#                 M = M+L
#                 L = 1
#     N=N+1
#
#     # 把L的等级情况生成一个序列储存起来。
#     list.append(L)
#     a = all_list(list)
# print(a)