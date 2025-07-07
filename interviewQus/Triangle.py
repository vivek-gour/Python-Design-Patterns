"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""


def solution(A):
    n = len(A)
    if n < 3:
        return 0  # Less than 3 elements cannot form a triangular triplet

    A.sort()  # Sort the array to simplify the triplet check

    for i in range(n - 2):
        # Check if A[i], A[i+1], A[i+2] can form a triangular triplet
        if A[i] + A[i + 1] > A[i + 2]:
            return 1  # Found a triangular triplet

    return 0  # No triangular triplet found


# Example usage:
print(solution([10, 2, 5, 1, 8, 20]))  # Should return 1
print(solution([10, 50, 5, 1]))  # Should return 0
print(solution([1, 2, 3]))  # Should return 1 (triplet (0, 1, 2))
print(solution([1, 2]))  # Should return 0 (not enough elements)