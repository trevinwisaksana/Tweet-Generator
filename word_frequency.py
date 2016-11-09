

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
def repeated_words_counter(text):
    # For loop through each object in array.
    for i in text:
        # If the word doesn't match
        if i not in repeated_words_list:
            # If it doesn't match, create a new array
            repeated_words_list.append([i.lower()])
            print("New array")
        # If the word already exists in the array.
        if i.lower() in repeated_words_list:
            # The index value of the word in the repeated_words_list array
            word_index = repeated_words_list.index(i.lower())
            # Append to the nested word array in the repeated_words_list
            repeated_words_list[word_index].append(i.lower())
            print("Appended again")


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


# Histogram Functions
def histogram(text):
    # Reading and splitting the words to be selectable.
    entire_text = text.read().split()
    # The repeated_words_counter to find similar words.
    repeated_words_counter(entire_text)


# Unique Words Function


# Frequency Function

if __name__ == "__main__":
    testing = histogram(source_text)
    # print(testing)
    list = repeated_words_list
    print(list)
