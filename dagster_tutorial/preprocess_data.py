'''Preprocess data dagster solid
'''
import pandas as pd
from dagster import op


@op
def preprocess_data(data):
    '''Preprocess data'''

    num_cols = [
        'calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo',
        'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups', 'rating']

    data_preprocessed = pd.DataFrame(data)
    data_preprocessed[num_cols] = data_preprocessed[num_cols].apply(pd.to_numeric)

    return data_preprocessed
