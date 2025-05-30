file = open("data_prog_contest_problem_2.txt", 'r')

line = []

with file as f:
    n, maxs = map(int, f.readline().strip().split())
    line = list(map(int, f.readline().strip().split()))
    
file.close()

line_set = set()

result = "NONE"

for i in range(n):
    if 1 <= line[i] <= maxs:
        line_set.add(line[i])

    if len(line_set) == maxs:
        result = i + 1
        break

print(result)
