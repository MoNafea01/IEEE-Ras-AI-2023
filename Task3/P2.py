"""
Given a list of integers, write a function to return the index of the
target. and if not found, sort the list and return the index of the target
if it would be inserted.
"""

list2 = [4, 2, 3, 1, 7]
target2 = 3
def fun_2(lst, t):
    if t in lst:
        return lst.index(t)
    else:
        lst.sort()
        for i in lst:
            if i > t:
                return lst.index(i)
        return len(lst)
      
