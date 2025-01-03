# extract the dataset from excel file
# train a model based on the data set

# Dataset Extraction
# we will be using pandas for this

import pandas as pd
import os
import sys

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
    
    print(list_sample_data_to_lowercase)
    

text_preprocessing()

# def test():
#     df = data_extraction()
#     print(df[])

# test()