"""
Take from user x number and prints the factorial of
number X
"""

nums3 = int(input("Enter number: "))
print(math.factorial(nums3))
fac = 1
for i in range(2, nums3+1):
    fac *= i
print(fac)
