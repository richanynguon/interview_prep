
from performance_tester import performance_tester


def matrix(n):
    matrix = []
    while len(matrix) < n:
        matrix.append(n*[0])
    counter = 1
    column = 0
    row = 0
    sequence = ["d", "l", "u", "r"]
    sequence_keeper = 0
    for i in range(((n+(n-1))//2)+1):
        if i is 0:
            for j in range(n):
                matrix[row][j] = counter
                counter += 1
                column = j
        else:
            for k in range(2):
                for l in range(n-i):
                    if sequence[sequence_keeper] == "d":
                        row += 1
                        matrix[row][column] = counter
                        counter += 1
                    elif sequence[sequence_keeper] == "l":
                        column -= 1
                        matrix[row][column] = counter
                        counter += 1
                    elif sequence[sequence_keeper] == "u":
                        row -= 1
                        matrix[row][column] = counter
                        counter += 1
                    elif sequence[sequence_keeper] == "r":
                        column += 1
                        matrix[row][column] = counter
                        counter += 1
                if sequence_keeper == 3:
                    sequence_keeper = 0
                elif sequence_keeper < 3:
                    sequence_keeper += 1

    return matrix

## rosetta code

def spiral_matrix(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m
for i in spiral_matrix(5): print(*i)


performance_tester([matrix, spiral_matrix], [3, 4, 25])
