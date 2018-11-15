# https://www.hackerrank.com/challenges/py-the-captains-room/problem

K = int(raw_input().strip())
rooms = map(int, raw_input().strip().split())

unique_rooms = set()
family_rooms = set()

for r in rooms:
    if r in unique_rooms:
        family_rooms.add(r)
    else:
        unique_rooms.add(r)

print list(unique_rooms.difference(family_rooms))[0]
