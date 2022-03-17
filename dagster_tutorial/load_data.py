'''Load data dagster solid
'''
import csv
import requests
from dagster import op


@op
def download_cereals():
    '''Load data'''
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return [row for row in csv.DictReader(lines)]
