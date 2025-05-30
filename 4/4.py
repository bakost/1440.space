def f(n: int) -> int:
    return int(str(n)[::-1])

def g(n: int) -> float:
    return f(f(n)) / n

g_values = {1}  # любой n, не заканчивающийся нулём, дает g(n)=1
for k in range(1, 30):
    g_values.add(1 / (10 ** k))

print(len(g_values))
