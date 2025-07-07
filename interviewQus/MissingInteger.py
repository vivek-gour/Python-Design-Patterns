"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution1(A):
    n = len(A)
    # Create a boolean array to track the presence of integers from 1 to N
    present = [False] * (n + 1)

    # Mark the integers that are present in the array
    for number in A:
        if 1 <= number <= n:
            present[number] = True

    # Find the smallest positive integer that is not present
    for i in range(1, n + 1):
        if not present[i]:
            return i

    # If all integers from 1 to N are present, return N + 1
    return n + 1


def solution2(A):
    # Implement your solution here
    remain = set(range(1, len(A)+1)) - set(A)
    return min(remain) if len(remain) != 0 else len(A) + 1