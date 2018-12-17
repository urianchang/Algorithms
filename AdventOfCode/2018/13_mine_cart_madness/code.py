# Python 3.7
"""
Each time a cart has the option to turn (by arriving at any intersection), it
turns left the first time, goes straight the second time, turns right the third
time, and then repeats those directions starting again.
"""


class Cart:
    def __init__(self, direction, x, y, turn):
        self.direction = direction
        self.x = x
        self.y = y
        self.turn = turn
        self.dead = False


def setup(file_lines):
    track = []
    carts = []
    for y, line in enumerate(file_lines):
        for x, ch in enumerate(line):
            if ch == "\n":
                continue
            if ch in "<v>^":
                direction = {
                    "<": "l",
                    "v": "d",
                    ">": "r",
                    "^": "u",
                }[ch]
                carts.append(Cart(direction, x, y, 'left'))
        track.append(line.strip('\n'))
    return track, carts


def move_cart(cart, mat):
    # type: (Cart, list) -> None
    if cart.direction == "d":
        cart.y += 1
    elif cart.direction == "u":
        cart.y -= 1
    elif cart.direction == "r":
        cart.x += 1
    elif cart.direction == "l":
        cart.x -= 1

    # For track turns
    bs = {
        "d": "r",
        "r": "d",
        "u": "l",
        "l": "u"
    }
    fs = {
        "d": "l",
        "r": "u",
        "l": "d",
        "u": "r"
    }

    next_step = mat[cart.y][cart.x]

    if next_step == "\\":
        cart.direction = bs[cart.direction]
    if next_step == "/":
        cart.direction = fs[cart.direction]
    if next_step == "+":
        if cart.turn == "left":
            cart.direction = {
                "l": "d",
                "d": "r",
                "r": "u",
                "u": "l"
            }[cart.direction]
        elif cart.turn == "right":
            cart.direction = {
                "r": "d",
                "d": "l",
                "l": "u",
                "u": "r"
            }[cart.direction]
        cart.turn = {
            "left": "straight",
            "straight": "right",
            "right": "left"
        }[cart.turn]


def tick_and_check_for_crashes(carts, map):
    sorted_carts = sorted(carts, key = lambda x: (x.y, x.x))
    collided = False
    for car in sorted_carts:
        move_cart(car, map)

        # Check if it collides with another cart
        positions = [(c.x, c.y) for c in sorted_carts]
        if len(set(positions)) != len(positions):
            collided = True
            break
    return collided


def run_p1():
    """Find the location of the first crash
    """
    matrix, carts = setup(open('input.txt').readlines())
    smooth = True
    count = 0
    while smooth:
        # print(f"Tick: {count}")
        did_collide = tick_and_check_for_crashes(carts, matrix)
        smooth = not did_collide
        count += 1

    positions = [(c.x, c.y) for c in carts]
    uniq = set()
    dupes = []
    for pos in positions:
        if pos not in uniq:
            uniq.add(pos)
        else:
            dupes.append(pos)

    assert len(dupes) == 1
    return (dupes[0][0], dupes[0][1])


def the_one(carts, matrix):
    tick = 0
    while len(carts) != 1:
        # print(f"Count: {tick}")
        sorted_carts = sorted(carts, key = lambda x: (x.y, x.x))
        collided = False
        for car in sorted_carts:
            if not car.dead:
                move_cart(car, matrix)

                # Check if it collides with another cart
                positions = [(c.x, c.y) for c in sorted_carts if not c.dead]
                if len(set(positions)) != len(positions):
                    for cr in sorted_carts:
                        if cr.x == car.x and cr.y == car.y:
                            cr.dead = True
        # Remove the dead carts
        carts = [c for c in carts if c.dead == False]
        tick += 1
    return carts[0]


def run_p2():
    """Find the location of the surviving cart
    """
    mat, carts = setup(open('input.txt').readlines())
    the_cart = the_one(carts, mat)
    return (the_cart.x, the_cart.y)


print(f"Part 1 - Collision @ {run_p1()}")   # 8,3
print(f"Part 2 - Last car @ {run_p2()}")    # 73,121
