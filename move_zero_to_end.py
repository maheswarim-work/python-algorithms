# play([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0])

# List comprehension

# expression
# iterable
# condition

# [expression for item in iterable if condition]

nums = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]

result = [non_zero for non_zero in nums if non_zero !=0 ] + [zero for zero in nums if zero==0]
print(result)
