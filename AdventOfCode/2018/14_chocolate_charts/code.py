# Python 3.7


def make_recipes(elf1, elf2, recipes):
    # type: (int, int, list) -> list
    combo = list(map(int, list(str(recipes[elf1] + recipes[elf2]))))
    # print(f"combo: {combo}, elf1: {elf1}, elf2: {elf2}, recipes: {recipes}")
    return combo


def run_elves_1(num: int) -> str:
    scores = [3, 7]
    elf1 = 0
    elf2 = 1
    while len(scores) <= (num+10):
        new = make_recipes(elf1, elf2, scores)
        scores.extend(new)
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

    return ''.join(map(str, scores[num:num+10]))


# Check that run_elves works with the examples
# assert run_elves_1(9) == "5158916779"
# assert run_elves_1(5) == "0124515891"
# assert run_elves_1(18) == "9251071085"
# assert run_elves_1(2018) == "5941429882"

p1 = run_elves_1(793031)
print(f"Part 1 - {p1}")  # 4910101614


def run_elves_2(num_str: str) -> int:
    scores = [3, 7]
    score_str = ''.join(map(str, scores))
    num_len = len(num_str)
    elf1 = 0
    elf2 = 1
    while True:
        new = make_recipes(elf1, elf2, scores)
        scores.extend(new)
        score_str += ''.join(map(str, new))
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

        if score_str[-num_len:] == num_str:
            return len(scores) - len(num_str)

        if score_str[-num_len-1:-1] == num_str:
            return len(scores) - len(num_str) - 1


# assert run_elves_2("51589") == 9
# assert run_elves_2("01245") == 5
# assert run_elves_2("92510") == 18
# assert run_elves_2("59414") == 2018

p2 = run_elves_2("793031")
print(f"Part 2 - {p2}") # 20253137
