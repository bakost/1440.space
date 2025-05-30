def recursion(index):
    f = [1, 3]
    A = []
    n = 0

    while len(A) <= index:
        if n >= len(f):
            f.append(5 * f[n - 1] + f[n - 2])
        
        if f[n] % 2 == 1:
            A.append(f[n])

        n += 1

    return A[index]

index = 39
result = recursion(index)
print("A[39] =", result)
