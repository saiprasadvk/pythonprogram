
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.


Sol::

def pairsock(n,ar):
    Sum = 0
    Dict = {}
    for i in ar:
        Dict[i] = ar.count(i)
    for x in Dict.values():
        Sum += x//2
    return Sum

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = pairsock(n, ar)
    print(result)
    
O/P:

9
10 20 20 10 10 30 50 10 20
3
