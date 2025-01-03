# extract the dataset from excel file
# train a model based on the data set

# Dataset Extraction
# we will be using pandas for this

import pandas as pd
import os
import sys

STOP_WORDS = [
    "a", "an", "the", "and", "or", "but", "so", "for", "nor", "yet", "in", "on", "at", 
    "by", "with", "about", "against", "between", "into", "through", "during", "before", 
    "after", "above", "below", "to", "from", "up", "down", "under", "over", "of", "off", 
    "I", "me", "my", "mine", "we", "us", "our", "ours", "you", "your", "yours", "he", 
    "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "theirs", 
    "is", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
    "will", "would", "shall", "should", "can", "could", "may", "might", "must", 
    "not", "very", "too", "then", "there", "here", "when", "where", "why", "how", 
    "do", "does", "did", "doing", "that", "this", "these", "those", "which", "what", 
    "who", "whom", "whose", "any", "each", "such", "only", "own", "same"
]

# file finder
def find_file_path(file):
    file_path = None
    sys.path.insert(0,"/home/john/Documents/fastapi/chats_with_intents/")
    for path in sys.path:
        pot_path = os.path.join(path, file)
        if os.path.exists(pot_path):
            file_path = pot_path
            break
    if file_path:
        return file_path
    else :
        return "No path for such file"


# data extractor
def data_extraction():
    file_path = find_file_path("dataSet.xlsx")
    df = pd.read_excel(file_path)
    #print(type(df))
    #df_list = df.values.tolist()
    return df


def text_preprocessing():
    # convert the text into lower case
    # remove words like "is", "the"
    # reduce words to the root form or lemmetization
    # tokenize sentences into words

    list_of_sample_data = data_extraction().values.tolist()
    
    #convert text to lowercase
    list_sample_data_to_lowercase = [list_of_sample_data[i][0].lower() for i in range(len(list_of_sample_data))]

    #remove the words like "is", "the" etc
    sample_without_stopwords = [list_sample_data_to_lowercase[i] for i in range(len(list_sample_data_to_lowercase))]
    print(sample_without_stopwords)
    

text_preprocessing()

# def test():
#     df = data_extraction()
#     print(df[])

# test()