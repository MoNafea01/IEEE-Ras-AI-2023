"""
Problem 4 🡪 Take from the user a list and remove duplicated items then
print it
"""

nums4 = input("Enter list separated by space: ").split() 
nums4_new = []
for i in nums4:
    if i not in nums4_new:
        nums4_new.append(i)
print(nums4_new)
