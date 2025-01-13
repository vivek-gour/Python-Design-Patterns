# is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.
# >>> a = [1, 2, 3]
# >>> b = a
# >>> b is a
# True
# >>> b == a
# True

# Make a new copy of list `a` via the slice operators,
# and assign it to variable `b`
# >>> b = a[:]
# >>> b is a
# False
# >>> b == a
# True
# In your case, the second test only works because Python caches small integer objects, which is an implementation detail. For larger integers, this does not work:
# >>> 1000 is 10**3
# False
# >>> 1000 == 10**3
# True
# The same holds true for string literals:
# >>> "a" is "a"
# True
# >>> "aa" is "a" * 2
# True
# >>> x = "a"
# >>> "aa" is x * 2
# False
# >>> "aa" is intern(x*2)
# True

# print(False == False == False)


def func(pattern, string):
    # Helper to check if a character is a vowel
    def is_vowel(char):
        return char in "aeiou"

    # Convert the pattern to a list of boolean checks
    pattern_check = [is_vowel if p == "0" else lambda c: not is_vowel(c) for p in pattern]
    print(pattern_check)
    pattern_length = len(pattern)
    count = 0

    # Slide over the string to check substrings
    for i in range(len(string) - pattern_length + 1):
        substring = string[i:i + pattern_length]
        # Check if the substring matches the pattern
        if all(check(substring[j]) for j, check in enumerate(pattern_check)):
            count += 1

    return count

# Example usage:
pattern = "010"
string = "amazing"
print(func(pattern, string))  # Output: 2





