sudoku = []
for _ in range(9):
    sudoku.append(list(map(int,input().strip())))
row_set = [[True for _ in range(10)] for _ in range(9)]
col_set = [[True for _ in range(10)] for _ in range(9)]
box_set = [[[True for _ in range(10)] for _ in range(3)] for _ in range(3)]

zero_list = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_list.append((i,j))
        else:
            row_set[i][sudoku[i][j]] = False
            col_set[j][sudoku[i][j]] = False
            box_set[i//3][j//3][sudoku[i][j]] = False


def is_ok(row, col, num):
    if row_set[row][num] and col_set[col][num] and box_set[row//3][col//3][num]:
        return True    
    return False

def solve_sudoku(idx):
    if idx == len(zero_list):
        return True
    r,c = zero_list[idx]
    for n in range(1,10):
        if is_ok(r,c,n):
            sudoku[r][c] = n
            row_set[r][n] = False
            col_set[c][n] = False
            box_set[r//3][c//3][n] = False
            if solve_sudoku(idx+1):
                return True
            row_set[r][n] = True
            col_set[c][n] = True
            box_set[r//3][c//3][n] = True
    return False

if solve_sudoku(0):
    for s in sudoku:
        print(*s,sep='')