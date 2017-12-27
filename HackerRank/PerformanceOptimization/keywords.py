"""
Keywords:

Given a paragraph 's' of space-separated lowercase English words and a list
of unique lowercase English keywords, find the minimum length of the
substring of 's' which contains all the keywords that are separated by space
in any order.

NOTE: Keywords should be space separated words but can occur in any order in
the substring.

If all the keywords aren't present in the paragraph, then print '-1'.
"""
def minimumLength(text, keys):
    # Submission 1: Default code - 10 / 100 (Last test case timed out)
    # answer = 10000000
    # text += " $"
    # for i in xrange(len(text) - 1):
    #     dup = list(keys)
    #     word = ""
    #     if i > 0 and text[i - 1] != ' ':
    #         continue
    #
    #     for j in xrange(i, len(text)):
    #         if text[j] == ' ':
    #             for k in xrange(len(dup)):
    #                 if dup[k] == word:
    #                     del(dup[k])
    #                     break
    #             word = ""
    #         else:
    #             word += text[j]
    #         if not dup:
    #             answer = min(answer, j - i)
    #             break
    #
    # if(answer == 10000000):
    #     answer = -1
    #
    # return answer

    # Submission 2: 0 / 100 - Runtime Error
    # textArr = text.strip().split()
    # d = {}
    # for i in xrange(len(textArr)):
    #     if textArr[i] in keys:
    #         if textArr[i] in d:
    #             d[textArr[i]].append(i)
    #         else:
    #             d[textArr[i]] = [i]
    # if len(d) != len(keys):
    #     return -1
    # else:
    #     c = [[]]
    #     for group in d.values():
    #         t = []
    #         for subgroup in group:
    #             for i in c:
    #                 t.append(i + [subgroup])
    #         c = t
    #     min_group = c[0]
    #     min_diff = 10000
    #     for group in c:
    #         total_diff = max(group) - min(group) + 1
    #         if total_diff < min_diff:
    #             min_diff = total_diff
    #             min_group = group
    #     count = -1
    #     for i in xrange(min(min_group), max(min_group)+1):
    #         count += len(textArr[i]) + 1
    #     return count

    # Submission 3: 0 / 100 - #13, 29, 30 wrong
    # textList = text.strip().split()
    # diff = 10000000000000
    # substring = []
    # for i in xrange(len(textList) - 1):
    #     if textList[i] in keys:
    #         dup = list(keys)
    #         dup.remove(textList[i])
    #         start = i
    #         for idx in xrange(i, len(textList)):
    #             if textList[idx] in dup:
    #                 dup.remove(textList[idx])
    #                 if len(dup) == 0:
    #                     end = idx
    #                     if (end-start) < diff:
    #                         diff = (end-start)
    #                         substring = textList[start:end+1]
    #
    # if diff == 10000000000000:
    #     return -1
    # else:
    #     return len(' '.join(substring))

    # Refactor Submission 3 to break out of loop early
    textList = text.strip().split()
    t = len(textList)
    k = len(keys)
    diff = 10000000000000
    for i in xrange(t - 1):
        if textList[i] not in keys:
            continue
        keys2 = list(keys)
        keys2.remove(textList[i])
        substring = len(textList[i])
        for idx in xrange(i+1, t):
            substring += len(textList[idx]) + 1
            if textList[idx] in keys2:
                keys2.remove(textList[idx])
                if len(keys2) == 0:
                    diff = min(diff, substring)
                    break

    if diff == 10000000000000:
        return -1
    else:
        return diff

    '''
    # *** Optimal solution ***
    max_length = 10000000

    def minimumLength(text, keys):
        answer = max_length
        text += " $"
        keys = set(keys)
        text = text.split()
        n = len(text)
        m = len(keys)
        for i in xrange(n-m+1):
            if text[i] not in keys:
                continue
            dup = set(keys)
            length = len(text[i])
            dup.remove(text[i])
            for j in xrange(i+1, n):
                length += len(text[j])+1
                if text[j] in dup:
                    dup.remove(text[j])
                    if not dup:
                        answer = min(answer, length)
                        break

        if(answer == max_length):
            answer = -1

        return answer
    '''

# Can't touch this stuff...
text = raw_input()
keyWords = int(raw_input())
keys = []
for i in xrange(keyWords):
    keys.append(raw_input())
print(minimumLength(text, keys))

"""
Input:
why how whywhat why what how what when what
3
why
how
what

Output:
12

Input:
why how what how when how when what
2
what
when

Output:
9
"""
