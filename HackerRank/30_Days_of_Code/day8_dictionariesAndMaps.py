"""
Day 8: Dictionaries and Maps

Given 'n' names and phone numbers, assemble a phone book
that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query
your phone book for. For each 'name' queried, print the
associated entry from your phone book on a new line in the form
'name=phoneNumber'; if an entry for 'name' is not found, print
'Not found' instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

n = int(raw_input().strip())
phoneBook = {}
for i in range(n):
    listing = raw_input().strip().split(' ')
    phoneBook[listing[0]] = listing[1]
for idx in range(n):
    query = raw_input().strip()
    if query in phoneBook:
        print query + "=" + phoneBook[query]
    else:
        print "Not found"
