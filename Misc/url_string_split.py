string = "postgresql+psycopg2://pactivbvw:p@postgres/pactivbvw"
string_list1 = string.split('/')
database = string_list1[-1]
string_list2 = string_list1[-2].split('@')
host = string_list2[1].split(':')
string_list3 = string_list2[0].split(':')
username = string_list3[0]
password = ''.join(string_list3[1:])

print username, password, host, database
