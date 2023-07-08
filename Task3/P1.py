"""
write a program to get the count of even numbers in a given list.
Make use of the lambda expression
"""

list1 = [5, 7, 7, 8, 8, 8, 10]
new_list1 = list(map(lambda n: n if (n % 2 == 0) else 0, list1))
new_list1 = [i for i in new_list1 if i != 0]
print(len(new_list1))
