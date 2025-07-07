"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""


def solution(A):
    n = len(A)
    if n == 0:
        return 0  # An empty array is not a permutation

    seen = set()
    for number in A:
        if number < 1 or number > n or number in seen:
            return 0  # Out of range or duplicate found
        seen.add(number)

    return 1 if len(seen) == n else 0  # Check if all numbers from 1 to N are present


# Example usage
print(solution([4, 1, 3, 2]))  # Should return 1
print(solution([4, 1, 3]))      # Should return 0
print(solution([]))             # Should return 0 (empty array)
print(solution([1, 2, 3, 4, 5]))  # Should return 1 (perfect permutation)
print(solution([1, 2, 2, 4]))  # Should return 0 (duplicate)
print(solution([1, 2, 3, 5]))  # Should return 0 (missing number)