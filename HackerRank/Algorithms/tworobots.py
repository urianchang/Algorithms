# n = int(raw_input().strip())
#
# def shortestPath(R1, R2, i, dist, arr):
#     if i == (len(arr) - 1):
#         if R2 == None:
#             return dist + abs(arr[i][0] - arr[i][1])
#         else:
#             return dist + abs(arr[i][0] - arr[i][1]) + min( abs(R1 - arr[i][0]), abs(R2 - arr[i][0]) )
#     if R2 == None:
#         R2 = arr[i][1]
#     dist += abs(arr[i][0] - arr[i][1])
#     return min( (abs(R1 - arr[i][0]) + dist + shortestPath(arr[i+1], R2, i+1, dist, arr)), (abs(R2 - arr[i][0]) + dist + shortestPath(R1, arr[i+1], i+1, dist, arr)) )
#
#
# while n != 0:
#     n -= 1
#     TC = map(int, raw_input().strip().split(' '))
#     queries = int(TC[1])
#     queryArr = []
#     for idx in range(queries):
#         query = map(int, raw_input().strip().split(' '))
#         queryArr.append(query)
#     test = shortestPath(queryArr[0][1], None, 1, abs(queryArr[0][1] - queryArr[0][0]), queryArr)
#     print test

n = int(raw_input().strip())

def shortestPath(R1, R2, i, dist, arr):
    if i == (len(arr) - 1):
        if R2 == None:
            return dist + abs(arr[i][0] - arr[i][1])
        else:
            return dist + abs(arr[i][0] - arr[i][1]) + min( abs(R1 - arr[i][0]), abs(R2 - arr[i][0]) )
    if R2 == None:
        R2 = arr[i][1]
    return abs(arr[i][0] - arr[i][1]) + min( (abs(R1 - int(arr[i][0])) + shortestPath(arr[i+1][1], R2, i+1, dist, arr)), (abs(R2 - int(arr[i][0])) + shortestPath(R1, arr[i+1][1], i+1, dist, arr)) )


while n != 0:
    TC = map(int, raw_input().strip().split(' '))
    queries = int(TC[1])
    n -= 1
    print n, queries
    queryArr = []
    for idx in range(queries):
        query = map(int, raw_input().strip().split(' '))
        queryArr.append(query)
    test = shortestPath(queryArr[0][1], None, 1, abs(queryArr[0][1] - queryArr[0][0]), queryArr)
    print test

    #     # TC += 2
    #     if R1 == None and R2 == None:
    #         distance += abs(start - end)
    #         R1 = end
    #     elif R1 != None and R2 == None:
    #         if abs(R1 - start) <= abs(start - end):
    #             distance += abs(R1 - start) + abs(start - end)
    #             R1 = end
    #         else:
    #             distance += abs(start - end)
    #             R2 = end
    #     elif R1 != None and R2 != None:
    #         R1_diff = abs(R1 - start)
    #         R2_diff = abs(R2 - start)
    #         if R1_diff <= R2_diff:
    #             distance += R1_diff + abs(start - end)
    #             R1 = end
    #         else:
    #             distance += R2_diff + abs(start - end)
    #             R2 = end
    # print distance
