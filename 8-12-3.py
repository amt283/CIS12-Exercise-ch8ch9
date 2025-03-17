"""“Wordle” is an online word game where the objective is to guess a five-letter word in six or fewer attempts. Each
attempt has to be recognized as a word, not including proper nouns. After each attempt, you get information about which
of the letters you guessed appear in the target word, and which ones are in the correct position.

For example, suppose the target word is MOWER and you guess TRIED. You would learn that E is in the word and in the
correct position, R is in the word but not in the correct position, and T, I, and D are not in the word.

As a different example, suppose you have guessed the words SPADE and CLERK, and you’ve learned that E is in the word,
but not in either of those positions, and none of the other letters appear in the word. Of the words in the word list,
how many could be the target word? Write a function called check_word that takes a five-letter word and checks whether
it could be the target word, given these guesses.

You can use any of the functions from the previous chapter, like uses_any."""
def main():
    #check_word('teeth')
    #check_word('grind')
    #check_word('mouth')
    check_word('exact')


def check_word(target_word):
    guess_num = 0
    guess_word = word_input(guess_num)
    while guess_num < 5:
        if guess_word == target_word:
            print("You guessed the word, congrats!")
        elif uses_any(guess_word, target_word):
            for i in range(len(target_word)):
                if guess_word[i] == target_word[i]:
                    print(f"Letter #{i+1}, \"{guess_word[i]}\" is in the correct spot!")
                elif guess_word[i] in target_word:
                    print(f"Letter #{i+1}, \"{guess_word[i]}\" is in the word, but it's in another spot!")
            guess_num += 1
            guess_word = word_input(guess_num)
        else:
            print("No letters correct")
            guess_num += 1
            guess_word = word_input(guess_num)

def word_input(guess_num):
    while True:
        guess_word = input(f"Guess #{guess_num + 1} - Choose a five letter word: ").strip()
        if len(guess_word) != 5:
            print(f"Error! Please pick a five letter word!")
        else:
            break
    return guess_word

def uses_any(word, letters):
    """Checks if any of the letters in 'letters' are used in 'word'."""
    for letter in letters:
        if letter in word:
            return True
    return False

if __name__ == "__main__":
    main()