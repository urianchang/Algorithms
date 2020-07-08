from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i, n in enumerate(nums):
        if n in map:
            map[n].append(i)
        else:
            map[n] = [i]

    for n in nums:
        d = target - n
        if d in map:
            if d == n:
                if len(map[d]) > 1:
                    return sorted(map[d])[:2]
                else:
                    continue
            else:
                return sorted([map[n][0], map[d][0]])


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([-3, 4, 3, 90], 0))
