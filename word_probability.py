# Importing the dict_histogram function
from word_frequency import dict_histogram
# Importing the random index chooser
from firstTweetGeneratorClass import random_index

# Opening the source text which is Beawulf.txt
source_text = open("Horatius.txt", "r")

# Modify the Shuffle method to:
#   Be able to pick more the words with higher probabilities

'''
SUDO CODE:
# We know the word frequency.
# Create a list that will put the repeated words consecutively
# Loop through the list to:
    # Use an random index picker
    # Append that to a list
    # Return that list
'''


# Probability based shuffler chooses words based on probability.
def loaded_dice(number_of_words_in_sentence, source_of_text):
    # List that contains the new random words.
    probability_based_word_list = []
    # Assigning the value of dict_histogram to text_dict
    text_dict = dict_histogram(source_of_text)
    # Basically making the dictionary a list
    # Converting the list because it lays out the same words beside each other.
    # This is useful when the randomizor picks the word as it has a higher
    # probability of being picked.
    dictionary_convereted_to_list = [value for value, count in text_dict.items() for i in range(count)]
    # Loop as much as the user wants the sentence length to be.
    for word in range(0, number_of_words_in_sentence):
        # Get a random index from the dictionary_convereted_to_list
        random_word_index = random_index(dictionary_convereted_to_list)
        # Append the words to the probability_based_word_list
        probability_based_word_list.append(dictionary_convereted_to_list[random_word_index])
    # Returning the list
    return probability_based_word_list


if __name__ == "__main__":
    testing = loaded_dice(5, source_text)
    print(testing)
