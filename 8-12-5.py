"""The Count of Monte Cristo is a novel by Alexandre Dumas that is considered a classic. Nevertheless, in the
introduction of an English translation of the book, the writer Umberto Eco confesses that he found the book to be
“one of the most badly written novels of all time”.

In particular, he says it is “shameless in its repetition of the same adjective,” and mentions in particular the
number of times “its characters either shudder or turn pale.”

To see whether his objection is valid, let’s count the number of lines that contain the word pale in any form,
including pale, pales, paled, and paleness, as well as the related word pallor. Use a single regular expression that
matches any of these words. As an additional challenge, make sure that it doesn’t match any other words, like impale –
you might want to ask a virtual assistant for help."""

import re

def main():
    match_list = ['pale', 'pales', 'paled', 'paleness', 'pallor']
    count_exact_word('CoMC.txt', match_list)

def count_exact_word(read_file, word_list):
    # Initialize a dictionary to store the word counts which are mapped to each word in the word_list
    word_counts = {}

    # Open the file and read its content, need to specify encoding='utf-8' because Gutenberg .txt file has characters
    # that aren't supported by default encoding and will create an UnicodeDecodeError.
    # https://docs.python.org/3/howto/unicode.html
    with open(read_file, 'r', encoding='utf-8') as reader:
        # The file is opened using with open() and the contents are saved in the text variable.
        text = reader.read()

        # Create a regex pattern to match any of the words in the list
        # re.escape() creates a regex pattern that matches any of the words in word_list, but re.escape() ensures that
        # each word is treated as a literal string, not as a regex pattern.
        # https://www.geeksforgeeks.org/regular-expression-python-examples/
        pattern = r'\b(' + '|'.join(map(re.escape, word_list)) + r')\b'

        # Find all matches of the words in the text
        matches = re.findall(pattern, text)

        # For each word in word_list, count how many times it appears in the matches list
        for word in word_list:
            word_counts[word] = matches.count(word)  # Count occurrences of each word

        # Print the results for each word in the list
        for word in word_counts:
            print(f"The word '{word}' appears {word_counts[word]} times in the novel.")

if __name__ == "__main__":
    main()