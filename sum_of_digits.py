# sum of digits until single digit recursion

def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    else:
        return digital_root(x)

num = 164221
print(digital_root(num))
