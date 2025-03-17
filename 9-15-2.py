"""Two words are anagrams if you can rearrange the letters from one to spell the other. For example, tops is an anagram
of stop.

One way to check whether two words are anagrams is to sort the letters in both words. If the lists of sorted letters
are the same, the words are anagrams.

Write a function called is_anagram that takes two strings and returns True if they are anagrams.

Using your function and the word list, find all the anagrams of takes."""

def main():
    print(is_anagram('stake', 'takes')) # true
    print(is_anagram('fire','takes')) # false
    print(is_anagram('steak', 'takes'))  # true
    print(is_anagram('skate', 'takes'))  # true
    print(is_anagram('skeet', 'takes'))  # false

def is_anagram(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    if sorted(list1) == sorted(list2):
        return True
    return False

if __name__ == "__main__":
    main()