'''
Find Duplicate Characters in a String Example: "programming" → r, g, m
'''

def duplicates():
    A="programming"

    duplicate = {}

    for i in A:
        if i in duplicate:
            duplicate[i] += 1
        else:
            duplicate[i] = 1

    for key,value in duplicate.items():
        if duplicate[key] > 1:
            print(key)
            '''If you do:

for item in frequency:
    print(item)

Output:

p
r
o

Only keys are returned.

To get both key and value:

for key, value in frequency.items():
    print(key, value)

Output:

p 1
r 2
o 1'''

duplicates()


