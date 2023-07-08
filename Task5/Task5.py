"""
Create a program to get the measures of spread of a list
[min,Q1, Q2, Q3, max], [range, IQR], [Variance, Standard deviation]
"""

from numpy import mean,var
my_list=[15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]


def measures_of_spread_of_list(my_list):
    my_list.sort()
    min_=my_list[0]
    max_=my_list[-1]
    if len(my_list) % 4 == 0:
        q1= (my_list[len(my_list) // 4 - 1] + my_list[len(my_list) // 4]) /2
        q2 = (my_list[len(my_list) // 2 - 1] + my_list[len(my_list) // 2]) / 2
        q3=(my_list[3*len(my_list) // 4 - 1] + my_list[3*len(my_list) // 4]) /2
    elif len(my_list) % 2 == 0 and len(my_list) %4 !=0:
        q1=(my_list[len(my_list) // 4])
        q2 = (my_list[len(my_list) // 2 - 1] + my_list[len(my_list) // 2]) / 2
        q3 = (my_list[3*len(my_list) // 4])
    elif len(my_list)//2 %2 != 0 :
        q1=(my_list[len(my_list) // 4])
        q2 = my_list[len(my_list)//2]
        q3 = (my_list[3*len(my_list) // 4])
    else:
        q1=(my_list[len(my_list) // 4 - 1] + my_list[len(my_list) // 4]) /2
        q2 = my_list[len(my_list)//2]
        q3 = (my_list[3*len(my_list) // 4 - 1] + my_list[3*len(my_list) // 4]) /2
    range_ = max_ - min_
    iqr_ = q3 - q1
    variance_ = sum((x-mean(my_list))** 2  for x in my_list) / (len(my_list)-1)
    sd_ = pow(variance_,0.5)
    print(my_list)
    return ([min_,q1,q2,q3,max_],[range_,iqr_],[variance_,sd_])

print(measures_of_spread_of_list(my_list))
