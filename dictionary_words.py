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
def random_index():
    rand_index = random.randint(0, 10)
    return rand_index


# Getting the entire text.
getting_entire_text = text_file.read()
print("=== getting_entire_text ===")
print(getting_entire_text)


# Getting a line from the text.
getting_one_line = text_file.readline()
print("=== getting_one_line ===")
print(getting_one_line)

# Closing the text_file.
text_file.close()
print("=== Closing Horatius.txt ===")
