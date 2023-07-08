"""
Make a function for Mean, Median, and Mode
"""

def mean_fun(my_list):
    sum_ = 0
    for i in my_list:
        sum_ += i
    return sum_ / len(my_list)

def median_fun(my_list):
    if len(my_list) % 2 == 0:
        return (my_list[int(len(my_list)/2) - 1] + my_list[int(len(my_list) / 2)]) / 2
    return my_list[int(len(my_list)/2)]

def mode_fun(my_list):
    max_nums = set(map(my_list.count, my_list))
    return [i for i in my_list if my_list.count(i) == max(max_nums)][0]

# Test
x = [1, 2, 2, 3, 4, 4, 4, 1]
print(mean_fun(x))
print(median_fun(x))
print(mode_fun(x))
