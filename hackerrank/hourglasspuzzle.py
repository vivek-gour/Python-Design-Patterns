__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'

import os


def hourglassSum(arr):
    out = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            try:
                hls = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
                out.append(hls)
            except Exception as e:
                print e.message
    return max(out)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
