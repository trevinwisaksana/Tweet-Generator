import random
# import shuffle

'''
SUDO CODE:
# Read a text in a file.
# Select a random set of words from the file.
    # for loop five times to choose five random words.
# Put those words together in a sentence.
'''

# Indicator for the Terminal.
print("=== Opening Horatius.txt ===")
# Opening Horatius.rtf
text_file = open("Horatius.txt", "r")


# Function that chooses a random index.
def random_index(text):
    rand_index = random.randint(0, len(text) - 1)
    return rand_index

# Getting a line from the text.
getting_entire_text = text_file.read()
print("=== getting_entire_text ===")
print(getting_entire_text)
print("=== splitting the lines ===")
splitted_list = getting_entire_text.split()
print(splitted_list)


# Function to shuffle the text.
def shuffle(text):
    # For-Loop that repeats the code 20 times.
    for i in range(0, 20):  # (len(text) * 2
        # Gets two random index value
        firstIndex = random_index(text)
        secondIndex = random_index(text)
        # Makes sure the two index values are not the same.
        while secondIndex == firstIndex:
            # If it's the same, repeat random index method.
            secondIndex = random_index(text)
            break
        text[firstIndex], text[secondIndex] = text[secondIndex], text[firstIndex]
    return text


# New scrambled list of text.
new_scrambled_list = shuffle(splitted_list)
# New sentence contains 5 random words from text.
new_sentence = []
# Loops five times to get 5 random words.
for i in range(0, 5):
    # Getting the random words using its random index value
    random_words_selected = random_index(new_scrambled_list)
    # Appending the new index number to the new_sentence array.
    new_sentence.append(new_scrambled_list[random_words_selected])

# Closing the text_file.
text_file.close()
print("=== Closing Horatius.txt ===")

'''
To make an autocorrect generator:
    # If we have a String as an argument for a function
    # We can .split() the String to seperate each alphabet
    # Find the first alphabet in using the 1 index number
    # e.g. if the alphabet is 'f', loop through the entire list of words
    # Split all the words so this will create arrays within arrays
    # Loop through the arrays to find if any of the first index value
      from any of the arrays matches the alphabet 'f'
    # Print all the arrays that matches the alphabet 'f'
    # Use the .join() method to undo the split method
'''

# Used to add space for the words.
# print(text, end=" ")
# This code runs and prints the quote chosen.
if __name__ == '__main__':
    print(new_sentence)
