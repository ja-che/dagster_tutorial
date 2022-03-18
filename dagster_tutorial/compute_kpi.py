'''Compute KPI dagster solids
'''
from dagster import op, Out


def find_highest_calorie_cereal(cereals):
    '''Compute first KPI'''
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["calories"]))
    return sorted_cereals[-1]["name"]


def find_highest_protein_cereal(cereals):
    '''Compute second KPI'''
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["protein"]))
    return sorted_cereals[-1]["name"]


def compute_model_accuracy(model, data_test, target_test):
    '''Compute model accuracy KPI'''
    accuracy = model.score(data_test, target_test)
    return accuracy


@op(out={"first_output": Out(), "second_output": Out(), "third_output": Out()})
def compute_kpi(data, model, data_test, target_test):
    '''Compute all KPIs'''
    highest_calorie_cereal = find_highest_calorie_cereal(data)
    highest_protein_cereal = find_highest_protein_cereal(data)
    accuracy = compute_model_accuracy(model, data_test, target_test)
    return highest_calorie_cereal, highest_protein_cereal, accuracy
