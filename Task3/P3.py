"""
given a list of integers , find the 4 integers in the list such that their
sum is closest to a target given. [No duplicates].
"""
list3 = [4, 2, 3, 1, 7, 12]
list3.sort()
target3 = 28


def min_num(lst, t):
    min_ = 1000
    for n in lst:
        if n < min_:
            min_ = n
    if t < min_:
        return 1
    return 0


def closest_nums(lst, t):
    if min_num(lst, t):
        return lst[0:4]
    if len(lst) <= 4:
        return lst
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                for m in range(k + 1, len(lst)):
                    if lst[i] + lst[j] + lst[k] + lst[m] == t:
                        return [lst[i], lst[j], lst[k], lst[m]]
                    if m == len(lst) - 1:
                        continue
                    if lst[i] + lst[j] + lst[k] + lst[m] > t:
                        if (lst[i] + lst[j] + lst[k] + lst[m]) - t < (lst[i - 1] + lst[j] + lst[k] + lst[m]) - t:
                            return [lst[i], lst[j], lst[k], lst[m]]
                        else:
                            return [lst[i - 1], lst[j], lst[k], lst[m]]
    return lst[-4:]


print(closest_nums(list3, target3))
