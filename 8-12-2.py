"""See if you can write a function that does the same thing as the shell command !head. It should take as arguments the
name of a file to read, the number of lines to read, and the name of the file to write the lines into. If the third
parameter is None, it should display the lines rather than write them to a file.

Consider asking a virtual assistant for help, but if you do, tell it not to use a with statement or a try statement."""

def main():
    #head_command('reading_file.txt', 10, 'writing_file.txt')
    #head_command('reading_file.txt', 5, None)
    #head_command_v2('reading_file.txt', 15, 'writing_file.txt')
    head_command_v2('reading_file.txt', 15, None)

# It's mentioned in the lecture that the better way of opening and reading a file is with the "with" statement so
# we'd be sure the file is closed afterward, but the exercise specifically mentioned not to use it, so I did it this
# way instead.
def head_command(read_file, line_num, write_file):
    read_object = open(read_file)
    counter = 0
    read_lines = ""
    for line in read_object:
        if counter < line_num:
            read_lines += line
            counter += 1
    if write_file is not None:
        write_object = open(write_file, 'w')
        write_object.write(read_lines)
        write_object.close()
    else:
        print(read_lines, end="")
    read_object.close()

# If I were to do the "head_command" function using "with" statements instead:
def head_command_v2(read_file, line_num, write_file):
    counter = 0
    read_lines = ""
    with open(read_file, "r") as reader:
        for line in reader:
            if counter < line_num:
                read_lines += line
                counter += 1
    if write_file is not None:
        with open(write_file, "w") as writer:
            writer.write(read_lines)
    else:
        print(read_lines, end="")

if __name__ == "__main__":
    main()