'''Dagster pipeline
'''
from dagster import job

from load_data import download_cereals
from preprocess_data import preprocess_data
from model import create_model
from compute_kpi import compute_kpi
from plot_kpi import display_results


@job
def my_pipeline():
    '''Dagster pipeline'''
    data = download_cereals()
    preprocessed_data = preprocess_data(data)
    model, data_test, target_test = create_model(preprocessed_data)
    most_calories, most_protein, accuracy = compute_kpi(
        data, model, data_test, target_test)
    _ = display_results(most_calories, most_protein, accuracy)


def main():
    '''Main function'''
    my_pipeline.execute_in_process()


if __name__ == '__main__':
    main()
