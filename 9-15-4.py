"""Write a function called reverse_sentence that takes as an argument a string that contains any number of words
separated by spaces. It should return a new string that contains the same words in reverse order. For example, if the
argument is “Reverse this sentence”, the result should be “Sentence this reverse”.

Hint: You can use the capitalize methods to capitalize the first word and convert the other words to lowercase."""

def main():
    print(reverse_sentence('This is what they say in reverse'))

# Reverses sentence word order and returns the reversed sentence with capitalized first word
def reverse_sentence(phrase):
    split_phrase = phrase.split() # split string by whitespace between words and saves as list
    reversed_split = reversed(split_phrase)
    return ' '.join(reversed_split).capitalize() # concatenate reversed list into string with first letter capitalized

if __name__ == "__main__":
    main()