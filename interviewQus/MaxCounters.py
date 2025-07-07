"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""


def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_max = 0

    for operation in A:
        if 1 <= operation <= N:
            # Increase the counter at position operation - 1
            if counters[operation - 1] < max_counter:
                counters[operation - 1] = max_counter
            counters[operation - 1] += 1
            current_max = max(current_max, counters[operation - 1])
        elif operation == N + 1:
            # Set all counters to the maximum value
            max_counter = current_max

    # Ensure all counters are at least the max_counter value
    for i in range(N):
        if counters[i] < max_counter:
            counters[i] = max_counter

    return counters


# Example usage:
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))  # Should return [3, 2, 2, 4, 2]
# Additional test cases
print(solution(3, [1, 2, 3, 4]))  # Should return [1, 1, 1]
print(solution(2, [1, 1, 2, 3]))  # Should return [2, 2]
print(solution(1, [1, 2, 1]))  # Should return [2]