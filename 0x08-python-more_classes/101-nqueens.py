#!/usr/bin/python3


import sys

def print_solution(queens):
    for row in queens:
        line = ['.'] * len(queens)
        line[row] = 'Q'
        print(''.join(line))

def is_safe(queens, row, col):
    for prev_row, prev_col in enumerate(queens):
        if prev_col == col or \
           prev_row + prev_col == row + col or \
           prev_row - prev_col == row - col:
            return False
    return True

def solve_nqueens(n):
    queens = [-1] * n
    solve(queens, 0, n)

def solve(queens, row, n):
    if row == n:
        print_solution(queens)
        print()
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve(queens, row + 1, n)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()

