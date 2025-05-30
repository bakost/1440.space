file = open("data_prog_contest_problem_1.txt", 'r')

points = []

with file as f:
    n = int(f.readline().strip())

    for _ in range(n):
        line = f.readline().strip()
        if line:
            start, end = map(int, line.split())
            points.append((start, end))

file.close()

points.sort(key=lambda interval: interval[1])

counter = 0
last_point = None

for start, end in points:
    if last_point is None or start > last_point:
        last_point = end
        counter += 1

print(counter)
