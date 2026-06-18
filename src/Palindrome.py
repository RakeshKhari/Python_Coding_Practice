'''4️⃣ Check if a String is Palindrome Example: "madam" → True'''

def palindrome():
    S="Madam"

    rev=""

    for i in range(len(S)):
        rev=S[i]+rev

    if rev.upper()==S.upper():
        print(f"{S} is Palindrome String")
    else:
        print(f"{S} is not Palindrome String")

palindrome()

'''What does * mean in print(*duplicate)?

The * is called the unpacking operator in Python.

Suppose:

duplicate = {'r', 'g', 'm'}

If you do:

print(duplicate)

Output:

{'r', 'g', 'm'}

The entire set is printed as one object.

Using *
print(*duplicate)

Python unpacks the set and passes each element separately to print().

It's equivalent to:

print('r', 'g', 'm')

Output:

r g m

(Actual order may vary because sets are unordered.)

Example with a List
A = [10, 20, 30]

print(A)

Output:

[10, 20, 30]

Now:

print(*A)

Output:

10 20 30

Python converts:

print(*A)

into:

print(10, 20, 30)
Example with Strings
name = "RAM"

print(*name)

Output:

R A M

Because Python unpacks the string into individual characters:

print('R', 'A', 'M')
Common Interview Use Cases
Convert list elements into function arguments
nums = [1, 2, 3]

def add(a, b, c):
    return a + b + c

print(add(*nums))

Output:

6

Python converts:

add(*nums)

to:

add(1, 2, 3)
Join elements while printing
A = [1, 2, 3, 4]

print(*A, sep="-")

Output:

1-2-3-4
In Your Duplicate Character Program
duplicate = {'r', 'g', 'm'}

print(*duplicate)

prints:

r g m

instead of:

{'r', 'g', 'm'}

So * simply means:

"Take all elements from this collection and pass them one by one."

This is one of the most frequently asked Python interview concepts,
 especially when discussing *args, unpacking lists, tuples, sets, and dictionaries.'''