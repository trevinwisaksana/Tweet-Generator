import random


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


# Getting the entire text.
# getting_entire_text = text_file.read()
# print("=== getting_entire_text ===")
# print(getting_entire_text)


# Getting a line from the text.
getting_one_line = text_file.readline()
print("=== getting_one_line ===")
print(getting_one_line)
print("=== splitting the lines ===")
splitted_string = getting_one_line.split()
print(splitted_string)


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
        # Stores first random number in tempValue
        text[firstIndex], text[secondIndex] = text[secondIndex], text[firstIndex]
    return text


# Closing the text_file.
text_file.close()
print("=== Closing Horatius.txt ===")


# This code runs and prints the quote chosen.
if __name__ == '__main__':
    new_sentence = shuffle(splitted_string)
    print(new_sentence)
