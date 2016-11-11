import random

# Quote that contains Monty Python's statement
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")


# Function that chooses a random sentence from the quotes.
def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]


# Text that contains texts that will be randomized.
''' Every single element should be printed but the
    only difference is that we have to reorder the
    text randomly when we print it.
'''
text = ["there", "is", "a", "bae", "cow", "here"]
# This is used to randomly place the randomly chosen word.

# DO NOT DO THIS! THIS IS AN ANTI-PATTERN.
# Imagine you have four tiles in front of you and the
# tile behind you is destroyed right after you walk
# to the next step.
''' # Incorrect function to randomize the text.
def random_text_quote():
    for object in text:
        # Choosing random integer
        rand_index = random.randint(0, len(text) - 1)
        # Appending the word with the same index.
        placeTextHere.append(text[rand_index])
        # Removing the item from the index.
        text.remove(text[rand_index])
    return placeTextHere
'''


# Cleaner code.
# Function to randomize the text.
'''
Sudo Code:
# If random_index returns two equal values, repeat randomizor.
# or
# If we receive the text
'''


# Function that chooses a random index.
def random_index(source_text):
    rand_index = random.randint(0, len(source_text) - 1)
    return rand_index


# Function to shuffle the text.
def random_text_quote():
    # For-Loop that repeats the code 20 times.
    for i in range(0, 20):
        firstIndex = random_index()
        secondIndex = random_index()
        while secondIndex == firstIndex:
            secondIndex = random_index()
            break
        text[firstIndex], text[secondIndex] = text[secondIndex], text[firstIndex]
    return text


# Function to reverse the string.
def reverse_sentence():
    numberOfIterations = len(text)/2
    # differenceInChange when indexNumber = 0
    for i in range(0, numberOfIterations):
        # Every index increment, the difference changes by -2.
        firstIndex = text[i]  # indexNumber is 0
        print("First index: ", firstIndex)
        secondIndex = text[-i - 1]
        print("Second index: ", secondIndex)
        text[i], text[-i - 1] = text[-i - 1], text[i]
        print("text: ", text)
    return text

# This code runs and prints the quote chosen.
if __name__ == '__main__':
    # First Challenge
    quote = random_python_quote()
    print(quote)
    # Second challenge
    # randomText = random_text_quote()
    # print(randomText)
    # Stretch Challenge 1
    strecthChallenge = reverse_sentence()
    print("Reversed Text: ", strecthChallenge)

    ''' # Second Challenge
        randomText = random_text_quote()
        # What ever that is left on the text array, add it.
        print(randomText + text)
    '''
