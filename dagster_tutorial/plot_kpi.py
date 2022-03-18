'''Plot KPI dagster solid
'''
from dagster import get_dagster_logger, op


@op
def display_results(most_calories, most_protein, accuracy=0.0):
    '''display computed KPIs'''
    logger = get_dagster_logger()
    logger.info(f"Most caloric cereal: {most_calories}")
    logger.info(f"Most protein-rich cereal: {most_protein}")
    logger.info(f"Model accuracy: {accuracy}")
    return None
