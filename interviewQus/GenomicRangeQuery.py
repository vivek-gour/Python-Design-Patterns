"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N - 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
"""

def solution(S, P, Q):
    N = len(S)
    M = len(P)

    # Create a prefix sum array for impact factors
    impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    prefix_sum = [[0] * (N + 1) for _ in range(4)]  # 4 types of nucleotides

    for i in range(N):
        nucleotide = S[i]
        for j in range(4):
            prefix_sum[j][i + 1] = prefix_sum[j][i] + (1 if impact_factors[nucleotide] == j + 1 else 0)

    result = []

    for k in range(M):
        start = P[k]
        end = Q[k] + 1  # Q is inclusive, so we need to go one past it

        # Check each nucleotide type's count in the range [start, end)
        for j in range(4):
            if prefix_sum[j][end] - prefix_sum[j][start] > 0:
                result.append(j + 1)  # Impact factor is j + 1
                break

    return result

def solution2(S, P, Q):
    # Implement your solution here
    dna = {"A": 1, "C": 2, "G": 3, "T": 4}
    return_list = []
    for val1, val2 in zip(P, Q):
        sub_str = S[val1:val2 + 1]
        temp_list = []
        for char in sub_str:
            temp_list.append(dna.get(char))
        return_list.append(min(temp_list))

    return return_list

# Example usage:
print(solution2("CAGCCTA", [2, 5, 0], [4, 5, 6]))  # Should return [2, 4, 1]
# Additional test cases
print(solution2("ACGT", [0, 1, 2], [3, 3, 3]))  # Should return [1, 2, 3]
print(solution2("TACG", [0, 1, 2], [3, 3, 3]))  # Should return [1, 2, 3]
print(solution2("GATC", [0, 1, 2], [3, 3, 3]))  # Should return [1, 2, 3]