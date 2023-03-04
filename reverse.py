n = [[1, 2], [3, 4], [5, 6, 7]]  # verilen input

def reverse(x):
    x= x[::-1]
    x= [y[::-1] for y in x]
    return x
print(reverse(n))