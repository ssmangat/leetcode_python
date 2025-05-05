# Solution for problem_36 is valid sudoku
# This problem appears complicated but can be divided into 3 parts
#1. 1 to 9 should appear only once in each of 9 rows,9 columns and 9 boxes
#2. we will use 9 hashsets for each of 9 rows, 9 columns and 9 boxes, so total 27 hashsets.
#3. Box calculation requires using a formula -> (row//3) * 3 + (column//3), which will give us the index of box.
def problem_36(board:list[list[str]]) -> bool:
    row_set = [set() for _ in range(9)] #9 sets for 9 rows
    col_set = [set() for _ in range(9)] #9 sets for 9 columns
    box_set = [set() for _ in range(9)] #9 sets for 9 boxes

    for i in range(9): #since we know board is 9 X 9
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue #continue the loop if current index is empty

            box_index = (i//3) * 3 + (j//3)
            if val in row_set[i] or val in col_set[j] or val in box_set[box_index]:
                return False

            row_set[i].add(val)
            col_set[j].add(val)
            box_set[box_index].add(val)

    return True
