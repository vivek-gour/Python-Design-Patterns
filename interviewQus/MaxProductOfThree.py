"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""

def solution1(A):
    A.sort()
    n = len(A)

    # The maximum product can be either:
    # 1. The product of the three largest numbers
    max_product1 = A[n-1] * A[n-2] * A[n-3]

    # 2. The product of the two smallest numbers (which could be negative) and the largest number
    max_product2 = A[0] * A[1] * A[n-1]

    return max(max_product1, max_product2)


def solution2(A):
    A.sort()

    # The maximum product can be either:
    # 1. The product of the three largest numbers
    max_product1 = A[-3] * A[-2] * A[-1]

    # 2. The product of the two smallest numbers (which could be negative) and the largest number
    max_product2 = A[0] * A[1] * A[-1]

    return max(max_product1, max_product2)

# Example usage:
print(solution1([-3, 1, 2, -2, 5, 6]))  # Should return 60
print(solution1([-10, -10, 1, 3, 2]))  # Should return 300
print(solution1([1, 2, 3]))  # Should return 6
print(solution([0, 0, 0]))  # Should return 0