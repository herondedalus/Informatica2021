#a super list, magical and exciting!
#dictionaries are a nice way of making a reference list! collezzioni di coppie, chiave valore, tipo sql

marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)
# Output: {'English': 0, 'Math': 0, 'Science': 0}
for item in marks.items():
 print(item)
list(sorted(marks.keys()))
# Output: ['English', 'Math', 'Science']


# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# remove a particular item
print(squares.pop(4))
print(squares) # Output: 16
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
# remove an arbitrary item
print(squares.popitem())
print(squares) # Output: (1, 1)
# Output: {2: 4, 3: 9, 5: 25}
# delete a particular item
del squares[3]
print(squares) # Output: {2: 4, 3: 9}
# remove all items
squares.clear()
print(squares) # Output: {}
# delete the dictionary itself
del squares
# print(squares)
# Throws Error