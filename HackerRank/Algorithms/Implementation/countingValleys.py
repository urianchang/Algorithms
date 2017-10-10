"""
Counting Valleys:

Gary is an avid hiker. He tracks his hikes meticulously, paying close
attention to small details like topography. During his last hike, he
took exactly n steps. For every step he took, he noted if it was
an uphill or a downhill step. Gary's hikes start and end at sea level. We
define the following terms:
    * A mountain is a non-empty sequence of consecutive steps above sea level,
    starting with a step up from sea level and ending with a step down to sea
    level.
    * A valley is a non-empty sequence of consecutive steps below sea level,
    starting with a step down from sea level and ending with a step up to sea
    level.

Given Gary's sequence of up and down steps during his last hike, find and
print the number of valleys he walked through.

Constraints:
    * 2 <= N <= 10^6
"""

N = int(raw_input().strip())
hike = raw_input().strip()

valleys, level = 0, 0

for step in hike:
    if step == "D":
        level -= 1
    else:
        level += 1
        # Only care about valleys: step up to sea level
        if level == 0:
            valleys += 1

print valleys

"""
Input:
8
UDDDUDUU

Output:
1
"""
