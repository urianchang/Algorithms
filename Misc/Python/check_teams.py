import typing

# For mocking API calls
TEAMS = {
    "A": {"members": ["a", "b"]},
    "B": {"members": ["b", "c"]},
    "D": {"members": ["d", "e", "f"]},
    "Z": {"members": ["z"]},
}


def filter_reviewers(reviewers: set, blacklist: typing.Union[list, str]) -> set:
    new = reviewers.copy()
    if blacklist is None:
        return new

    if isinstance(blacklist, str):
        if blacklist == "DELETE_ALL":
            return set()
        else:
            print(f"Unsupported option for filtering reviewers: {blacklist}")
    elif isinstance(blacklist, list):
        return new.difference(set(blacklist))
    else:
        print(f"Unsupported type for filtering reviewers: {type(blacklist)}")

    # If anything goes wrong, return unmodified copy
    return new


def update_requested_reviewers(
    current_users,
    current_teams,
    remove_reviewers,
    add_reviewers,
    remove_team_reviewers,
    add_teams,
) -> None:
    required_teams = filter_reviewers(current_teams, remove_team_reviewers)
    if add_teams:
        required_teams = required_teams | set(add_teams)

    required_users = filter_reviewers(current_users, remove_reviewers)
    if add_reviewers:
        required_users = required_users | set(add_reviewers)

    # Get list of users for required_teams (API calls)
    team_members = {}
    for team in required_teams:
        team_members[team] = set(TEAMS[team]['members'])

    # Get users for required_teams
    approved_users = set()
    for members in team_members.values():
        approved_users = approved_users | members

    # Get users to remove because they don't match any of the required teams
    delete_users = set(current_users).difference(approved_users | required_users)
    
    # Teams to delete
    remove_teams = set(current_teams).difference(required_teams)

    # Get users to keep
    keep_users = set(current_users).difference(delete_users)

    # Add users if necessary
    add_users = required_users.difference(keep_users)

    # Add teams if necessary
    add_teams = set()
    for team in required_teams:
        if team not in current_teams and len(team_members[team].intersection(keep_users | add_users)) == 0:
            add_teams.add(team)

    print(f"USERS... current: {current_users}, required: {required_users}, remove: {delete_users}, add: {add_users}")
    print(f"TEAMS... current: {current_teams}, required: {required_teams}, remove: {remove_teams}, add: {add_teams}")


current_users = set(["a", "b", "c", "d"])
current_teams = set(["A"])

remove_reviewers = "DELETE_ALL"
remove_team_reviewers = "DELETE_ALL"

add_reviewers = ["y", "d"]
add_teams = ["B", "D", "Z"]

update_requested_reviewers(
    current_users, 
    current_teams, 
    remove_reviewers, 
    add_reviewers, 
    remove_team_reviewers, 
    add_teams
)
"""Expected
USERS... current: ['a', 'b', 'c', 'd'], required: {'y', 'd'}, remove: {'a'}, add: {'y'}
TEAMS... current: ['A'], required: {'Z', 'D', 'B'}, remove: {'A'}, add: {'Z'}
"""

update_requested_reviewers(
    current_users, 
    set(), 
    ["d"], 
    [], 
    [], 
    [],
)
"""Expected
USERS... current: {'c', 'b', 'd', 'a'}, required: {'c', 'b', 'a'}, remove: {'d'}, add: set()
TEAMS... current: set(), required: set(), remove: set(), add: set()
"""

update_requested_reviewers(
    current_users, 
    set(), 
    "DELETE_ALL", 
    [], 
    "DELETE_ALL", 
    ["Z"],
)
"""Expected
USERS... current: {'b', 'c', 'a', 'd'}, required: set(), remove: {'b', 'c', 'a', 'd'}, add: set()
TEAMS... current: set(), required: {'Z'}, remove: set(), add: {'Z'}
"""

update_requested_reviewers(
    set(["a", "z"]), 
    set(["A", "B"]), 
    "DELETE_ALL", 
    [], 
    "DELETE_ALL", 
    ["Z"],
)
"""Expected
USERS... current: {'z', 'a'}, required: set(), remove: {'a'}, add: set()
TEAMS... current: {'A', 'B'}, required: {'Z'}, remove: {'A', 'B'}, add: set()
"""

update_requested_reviewers(
    set(), 
    set(["Z"]), 
    "DELETE_ALL", 
    [], 
    "DELETE_ALL", 
    ["Z"],
)
"""Expected
USERS... current: set(), required: set(), remove: set(), add: set()
TEAMS... current: {'Z'}, required: {'Z'}, remove: set(), add: set()
"""

update_requested_reviewers(
    set(["a"]), 
    set(["Z"]), 
    "DELETE_ALL", 
    ["a"], 
    "DELETE_ALL", 
    [],
)
"""Expected
USERS... current: {'a'}, required: {'a'}, remove: set(), add: set()
TEAMS... current: {'Z'}, required: set(), remove: {'Z'}, add: set()
"""

update_requested_reviewers(
    set(["a", "b"]), 
    set(), 
    "DELETE_ALL", 
    ["a"], 
    "DELETE_ALL", 
    [],
)
"""Expected
USERS... current: {'b', 'a'}, required: {'a'}, remove: {'b'}, add: set()
TEAMS... current: set(), required: set(), remove: set(), add: set()
"""
