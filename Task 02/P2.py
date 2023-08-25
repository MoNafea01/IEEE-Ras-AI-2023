"""
Take from user three numbers A, B, and C, and print them in
ascending order in one line.
"""
nums2 = input("Enter numbers separated by space: ").split()
nums2 = [int(i) for i in nums2]
nums2.sort()
print(' '.join(str(e) for e in nums2))
