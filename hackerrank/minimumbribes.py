__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018, Vivek Gour'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Viv30ek@searce.com'
__status__ = 'Learning'


def minimumBribes(q):
    tempArr = range(1, len(q) + 1)
    bribe = 0
    for qIndex in xrange(len(q)):
        tempArrIndex = tempArr.index(q[qIndex])
        tooChaotic = 0
        while tempArrIndex != qIndex:
            tempArr[tempArrIndex], tempArr[tempArrIndex - 1] = tempArr[tempArrIndex - 1], tempArr[tempArrIndex]
            tempArrIndex -= 1
            bribe += 1
            tooChaotic += 1
            if tooChaotic > 2:
                print("Too chaotic")
                return
    print(bribe)


if __name__ == '__main__':
    # t = int(raw_input())
    #
    # for t_itr in xrange(t):
    #     n = int(raw_input())
    #
    #     q = map(int, raw_input().rstrip().split())

    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 2, 5, 3, 7, 8, 6, 4]
