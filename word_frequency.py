

"""
A histogram() function which takes a source_text argument
(can be either a filename or the contents of the file as a string, your choice)
and return a histogram data structure that stores each unique word along with
the number of times the word appears in the source text.

A unique_words() function that takes a histogram argument and returns the total
count of unique words in the histogram. For example, when given the histogram
for The Adventures of Sherlock Holmes, it returns the integer 8475.

A frequency() function that takes a word and histogram argument and returns the
number of times that word appears in a text. For example, when given the word
"mystery" and the Holmes histogram, it will return the integer 20.
"""

# Opening the source text which is Beawulf.txt
source_text = open("Horatius.txt", "r")


# Contains a list of repeated words
repeated_words_list = []
# repeated_words_list = [[] for i in range(0, len(entire_text))]


# An function that stores the word in the repeated_words_list
def histogram(text):
    # Reading and splitting the words to be selectable.
    entire_text = text.read().split()
    # For loop through each object in array.
    for i in range(0, len(entire_text)):
        # Contains the word
        any_word = entire_text[i]
        # If a word from entire_text matches with a word in repeated_words_list
        if any(any_word in entire_text for any_word in repeated_words_list):
            # If it matches with a word
            repeated_words_list[i].append([any_word.lower()])
            print("Appended to existing array")
        repeated_words_list.append([any_word.lower()])
        print("New array")


# A function that uses dictionaries as a word counter.
def repeated_words_counter_dict(text):
    # Entire text
    entire_splitted_text = text.read().split()
    # Dictionary that contains the new word
    word_dict = {}
    # Loops through each word in the entire text
    for word in text:


'''
SUDO CODE:
# Loop through the words that are in the entire_text
# If there are words that matches, add it to an existing array
  with the same word
# If the it doesn't match with any other word, create a new array
# Count the number of words within each nested array to get the frequency and
  unique words
# If the words are used less than 5 times, they are unique
# If not, they are are commonly used words
'''

if __name__ == "__main__":
    testing = histogram(source_text)
    # print(testing)
    list = repeated_words_list
    print("Repeated Words List: ", list)
