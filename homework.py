# def get_max_num(nums: list):
#     if len(nums) == 0:
#         return 0, False
#
#     res = nums[-1]
#     for num in nums:
#         if num > res:
#             res = num
#
#     return res, True
#
#
# def get_arithmetic_mean(lst_nums):
#     res = 0
#     for i in lst_nums:
#         res += i
#     return res / len(lst_nums)
#
#
# def sorted(nums):
#     for i in range(len(nums)):
#         for u in range(0, len(nums) - 1):
#             if nums[u] > nums[u + 1]:
#                 nums[u], nums[u + 1] = nums[u + 1], nums[u]
#     return nums
#
#
# print(sorted([6, 5, 4, 3, 7, 1]))
# print(get_max_num([1, 2, 3, 4, 5, 6]))
# print(get_arithmetic_mean([1, 2, 4, 3, 6]))


# n = int(input())
#
# for i in range(1, n+1):
#     print(f"{i} + {n} = {i * n}")


# str = input()
# slovar = {}
#
# for i in str:
#     slovar[i] = str.count(i)
#
# max_str = max(slovar, key=slovar.get)
# print(max_str)
#
# new_str = ""
# for u in str:
#     if not u in [".", " ", ",", "!", "?"]:
#         new_str += u
#
# print(new_str)


def factors(n):
    res = []
    for i in range(1, n + 1):
        if str(n / i)[-1] == "0" and str(n / i)[-2] == ".":
            res.append(i)
    return res


def common_factors(a, b):
    res = []
    min_num = min([a, b])
    for i in range(1, min_num):
        if str(a / i)[-1] == "0" and str(a / i)[-2] == "." and str(b / i)[-1] == "0" and str(b / i)[-2] == ".":
            res.append(i)

    return res


print(factors(10))
print(common_factors(10, 15))