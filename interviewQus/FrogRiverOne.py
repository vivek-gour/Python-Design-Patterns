"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""


def solution1(X, A):
    positions = set()  # To track the positions covered by leaves
    for time, position in enumerate(A):
        if position <= X:  # Only consider positions within the range [1..X]
            positions.add(position)
        if len(positions) == X:  # If all positions from 1 to X are covered
            return time  # Return the earliest time when frog can jump
    return -1  # If not all positions are covered, return -1


def solution2(X, A):
    if len(A) < X:
        return -1
    elif len(A) == X and len(A) == 1:
        return 0 if set(A) == set(range(1, X + 1)) else -1
    elif len(A) == X and len(A) != 1 and set(A) == set(range(1, X + 1)):
        return X - 1
    elif len(A) == X and len(A) != 1 and set(A) != set(range(1, X + 1)):
        return -1

    for val in range(X, len(A) + 1):
        if set(A[:val]) == set(range(1, X + 1)):
            return val - 1

    return -1

print(solution2(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # Example usage# Should return 6
print(solution2(5, [1, 2, 3, 4, 5]))  # Should return 4
print(solution2(5, [1, 2, 3, 4, 6]))  # Should return -1
print(solution2(5, [1, 2, 3, 4]))  # Should return -1 (not all positions covered)
print(solution2(1, [1]))  # Should return 0 (immediate jump possible)
print(solution2(1, [2]))  # Should return -1 (jump not possible)
