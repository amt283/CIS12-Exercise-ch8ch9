"""Write a function called total_length that takes a list of strings and returns the total length of the strings. """

def main():
    list1 = ['one']
    list2 = ['one', 'two']
    list3 = ['one', 'two', 'three']

    print(total_length(list1)) # Three
    print(total_length(list2))  # Six
    print(total_length(list3))  # Eleven

# Takes length of each string in a list and returns the total length of all strings (combined)
def total_length(string_list):
    sum_length = 0
    for i in string_list:
        sum_length += len(i)
    return sum_length

if __name__ == "__main__":
    main()