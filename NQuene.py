# Simple N Queen Program

n = 4

board = [0] * n


def safe(row, col):

    for i in range(col):

        # Same row
        if board[i] == row:
            return False

        # Diagonal check
        if abs(board[i] - row) == abs(i - col):
            return False

    return True


def queen(col):

    if col == n:
        return True

    for row in range(n):

        if safe(row, col):

            board[col] = row

            if queen(col + 1):
                return True

    return False


queen(0)

print("Solution is :\n")

for i in range(n):

    for j in range(n):

        if board[j] == i:
            print("Q", end=" ")

        else:
            print(".", end=" ")

    print()