def reverse():
    A = "Palindrome String"
    rev = ""

    for i in A:
        rev=i + rev

    '''charAt() is a Java method, not available in Python.
In for i in A:, i is already a character, not an index.
The print(rev) is inside the loop, so it prints after every iteration.

def reverse():
    A = "Palindrome String"
    rev = ""

    for i in range(len(A)):  // if using range it gives the index and using 
                                direct A give character directly
        rev = A[i] + rev   // Python uses square brackets [] 
                              directly for indexing, so there is no charAt() method.
    print(rev)
    
reverse()

'''

    print(rev)

reverse()