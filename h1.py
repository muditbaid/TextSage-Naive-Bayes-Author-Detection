from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from text_utilities import *
import pandas as pd
from pathlib import Path

# Assuming you have a list of file names in the 'files' variable
# files = ['Alcott-Lousia May-Eight Cousins.txt',
#     "Alcott-Lousia May-Jo's Boys.txt",
#     # Add other file names here
# ]

# Create an empty list to store authors
# def create_train_data():
#     authors = []
#     texts = []
#     train_files = text_utilities.train_files

#     for file in train_files:
#         author = text_utilities.get_author_from_filename(file)
#         text = text_utilities.read_file(file)
#         tokens = text_utilities.tokenize(text)

#         authors.append(author)

#     # Create a DataFrame with 'File' and 'Author' columns
#     train_df = pd.DataFrame({'Author': authors})
#     return train_df

# # Display the DataFrame
# print(create_train_data())

train_df = generate_training_data()
train_df.head()