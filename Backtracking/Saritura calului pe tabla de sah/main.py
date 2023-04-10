def inside(table, line, col):
    return line >= 0 and line < len(table) and col >= 0 and col < len(table)

def consistent(table, possible_line, possible_col):
    return inside(table, possible_line, possible_col) and not table[possible_line][possible_col]

def printTable(table):
    for line in range(len(table)):
        for col in range(len(table)):
            print(table[line][col], end = ' ')
            #print('*', end = '') if table[line][col] == 2 else print('#', end = '')
        print()
    print()

def back(table, line = 0, col = 0, dir = [[2, 1], [1, 2], [2, -1], [-1, 2], [-2, 1], [1, -2], [-2, -1], [-1, -2]]):
    printTable(table)
    for d in dir:
        possible_line, possible_col = line + d[0], col + d[1]
        if consistent(table, possible_line, possible_col):
            table[line][col], table[possible_line][possible_col] = 1, 2
            back(table, possible_line, possible_col, dir)
            table[line][col], table[possible_line][possible_col] = 2, 0

def main():
    N = int(input('N = '))
    table = [[0 for i in range(N)] for j in range(N)]
    table[0][0] = 2
    back(table)

main()