# https://www.reddit.com/r/adventofcode/comments/a61ojp/2018_day_14_solutions/ebr8abv/

recipes = open('day14.in','r').read().strip()

score = '37'
elf1 = 0
elf2 = 1
while recipes not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

print('Part 1:', score[int(recipes):int(recipes)+10])
print('Part 2:', score.index(recipes))
