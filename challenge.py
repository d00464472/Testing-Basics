# Challenge:
# Write a function called is_palindrome(word) that returns True if the
# given word reads the same forwards and backwards, and False otherwise.
#
# Examples:
# is_palindrome("racecar") -> True
# is_palindrome("hello") -> False
# is_palindrome("level") -> True


def is_palindrome(word):
    return word == word[::-1]
