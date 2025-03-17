# CIS 12, Ch 8 & 9 Exercises

<h2>Exercise 8.12.2</h2>

Both my version and the instructor's version are the same, more or less. The exercise in the chapter mentioned telling 
the Virtual Assistant not to use with or try statements, so I took that to mean that the exercise didn't want me to use 
them either which is why I decided to make two versions of the same function. Even if this wasn't what the exercise was 
asking for, I think it was good practice because it helped me see how useful the with statements are since I didn't 
have to worry about where to put the .close() - something that gave me a bit of trouble in the first version of the 
function considering it needed to stay within the if-statement scope. That and the version with the with statements was 
much cleaner and easier to read. 

<h2>Exercise 8.12.3</h2>

Oops, I misunderstood the exercise and, consequently, ended up making a script that <i> almost</i> makes a Wordle game. 
For this reason, my version only vaguely resembles the instructor's, so I can't really say which version is better. 
Though I can say that my version could use improvements. I'm sure there's ways I can trim down my code, but I also 
couldn't quite get it to work the way I intended and I couldn't figure out how to fix it (entirely because I was 
doing way more than what the exercise was asking for, so that figures.) The problem I was running into was that my 
script would check the five letter input word and determine if any of the letters used in the input word could be 
found in the target word (so if the target word was "exacty", a guess word of "entre" would tell the user that they
correctly guessed the first letter). However, what the script was also supposed to do was give a hint when the player
guessed a correct letter but in the wrong position - so, "apple" would tell the user they guessed e correctly, but
it's in the wrong spot. The problem I ran into was that if I used "entre" the game to tell the user incorrect info - 
that the first letter was guessed correctly, but that the last e in the word was ALSO correct and just in the wrong
spot (when it's not) which implies that the target word has two e's when it only has one. So, since the program is 
already way off from the exercise, the only way I can think to improve it is to figure out how to keep track of the 
letters to avoid giving out wrong hints if there are too many of the same letter.

<h2>Exercise 8.12.5</h2>

When comparing the two versions, I can easily say the instructor's version is better. I didn't think to use a regular 
expression for the words I needed to match, so I think the instructor's version is more efficient, much cleaner and 
much easier to read. I don't think my version is bad, but I think it could definitely be cleaned up considering I 
wasn't quite sure what I was doing and was just doing my best to get something that both made sense and worked, which 
doesn't make for neat code. So I think I could definitely trim some things and condense redundant lines.

<h2>Exercise 9.15.2</h2>

This was another exercise I misunderstood. The exercises kept mentioning a wordlist and I had no idea what it was 
referring to, so I figured it was a rhetorical thing. Either way, I did the majority of the exercise, at least, and it 
looks like both my version and the instructor's version are pretty much the same. Though the instructor's version 
compares the length of the words and I'm not sure why that's necessary - wouldn't sorting the lists and see if the 
lists are the same be enough? If a list is ['a', 'b', 'c'] and another is ['a', 'b', 'c', 'd'] does it consider both 
the same because the first three items are the same, hence why you'd need to check the length?

<h2>Exercise 9.15.3</h2>

My version and the instructor's are the same, more or less, though mine is understandably missing anything related 
to the word list.

<h2>Exercise 9.15.4</h2>

My version and the instructor's are the same, more or less, though  the instructor's is a little cleaner since I 
didn't think to condense everything down to a single line for the reverse_sentence function. Despite this, I somewhat 
prefer my version for the sake of readability and being able to quickly understand what the function is doing. Though 
that's probably more to do with all of this still being pretty new to me, so I need things spaced out a bit more.

<h2>Exercise 9.15.5</h2>

My version and the instructor's are the same, more or less, though  the instructor's is a little cleaner since I 
didn't think to condense everything down to a single line for the total length function. Despite this, I somewhat 
prefer my version for the sake of readability and being able to quickly understand what the function is doing. Though 
that's probably more to do with all of this still being pretty new to me, so I need things spaced out a bit more.