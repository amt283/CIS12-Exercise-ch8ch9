"""A palindrome is a word that is spelled the same backward and forward, like “noon” and “rotator”. Write a function
called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise."""

def main():
    print(is_palindrome('noon')) # True
    print(is_palindrome('root'))  # False

# Determines if word is a palindrome (spelled the same forward and backwards)
def is_palindrome(word):
    if word == reverse_word(word):
        return True
    return False

# Function that reverses a string and returns it, can't just use reversed() on a string
def reverse_word(word):
    return ''.join(reversed(word))

if __name__ == "__main__":
    main()