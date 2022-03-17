'''Dagster pipeline
'''
from dagster import job

from load_data import download_cereals
from compute_kpi import compute_kpi
from plot_kpi import display_results


@job
def my_pipeline():
    '''Dagster pipeline'''
    cereals = download_cereals()
    most_calories, most_protein = compute_kpi(cereals)
    _ = display_results(most_calories, most_protein)


def main():
    '''Main function'''
    my_pipeline.execute_in_process()


if __name__ == '__main__':
    main()
