import random

teamList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14]

random.shuffle(teamList)

count = 4

left = len(teamList) % count
each = len(teamList) // count

print('|-- ' + str(left))
print('|-- ' + str(each))

print(35/9)
