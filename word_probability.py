# Importing the dict_histogram function
from word_frequency import dict_histogram

# Opening the source text which is Beawulf.txt
source_text = open("Horatius.txt", "r")

# Modify the Shuffle method to:
#   Be able to pick more the words with higher probabilities

'''
SUDO CODE:
# We know the word frequency.
# Find the number of words that are in the text
  to get word_frequency/total_number_of_words.
# Use the word picker which has an if statment that checks
    # For loop through inside the splitted text
    # if the word is used more than  25%/50%/75%  ('/' refers to 'or') of
      the total words.
        #
'''

# List that contains the new random words.
probability_based_word_list = []


# Probability based shuffler chooses words based on probability.
def loaded_dice(number_of_words_in_sentence, array_input, source_of_text):
    # Assigning the value of dict_histogram to text_dict
    text_dict = dict_histogram(source_of_text)



if __name__ == "__main__":
    # testing = dict_histogram(source_text)
