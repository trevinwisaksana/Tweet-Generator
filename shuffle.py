import random


# Contains the objects.
text = ["there", "is", "a", "cow"]


# Function that chooses a random index.
def random_index():
    rand_index = random.randint(0, len(text) - 1)
    return rand_index


# Function to shuffle the text.
def shuffle():
    # For-Loop that repeats the code 20 times.
    for i in range(0, 20):  # (len(text) * 2
        # Gets two random index value
        firstIndex = random_index()
        secondIndex = random_index()
        # Makes sure the two index values are not the same.
        while secondIndex == firstIndex:
            # If it's the same, repeat random index method.
            secondIndex = random_index()
            break
        # Stores first random number in tempValue
        # tempValue = text[firstIndex]
        # text[firstIndex] = text[secondIndex]
        # text[secondIndex] = tempValue
        text[firstIndex], text[secondIndex] = text[secondIndex], text[firstIndex]
    return text


# This code runs and prints the quote chosen.
if __name__ == '__main__':
    randomText = shuffle()
    print(randomText)
