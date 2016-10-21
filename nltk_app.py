

import nltk
from nltk import word_tokenize, pos_tag
import string

# Get all the English alphabet letters and a space
valid_letters = string.letters + ' '
#############
# Example 1 #
#############

text = "Hello, how are you?"

# Remove all punctuation
stripped_text = ''.join([char if char in valid_letters else '' for char in text])
print (stripped_text)
# OUTPUT: 'Hello how are you'

# Tokenize
tokens = word_tokenize(stripped_text)
print (tokens)
# OUTPUT:  ['Hello', 'how', 'are', 'you']

# Get POS
tags = pos_tag(tokens)

'''
If you print the tags variable you will get the following output

[('Hello', 'NNP'), ('how', 'WRB'), ('are', 'VBP'), ('you', 'PRP')]
NNP = singular proper noun
WRB = WH adverb
VBP = verb, present tense, not 3rd person singular
PRP = pronoun, personal
'''


#############
# Example 2 #
#############

# We do the same process as before
text = "What is the value of Apple stock?"
stripped_text = ''.join([char if char in valid_letters else '' for char in text])
tokens = word_tokenize(stripped_text)
tags = pos_tag(tokens)

'''
If we print the tags variable:
[('What', 'WP'),
 ('is', 'VBZ'),
 ('the', 'DT'),
 ('value', 'NN'),
 ('of', 'IN'),
 ('Apple', 'NNP'),
 ('stock', 'NN')]
 '''