'''Model dagster solid
'''
from dagster import op, Out

from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split


def load_model(data):
    '''Load model'''

    model = RidgeCV()

    features = [
        'calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo',
        'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups']

    target = 'rating'

    return model, data[features], data[target]


def fit_model(model, features, target):
    '''Fit model'''

    data_train, data_test, target_train, target_test = train_test_split(
        features, target, random_state=42, test_size=0.3)

    model.fit(data_train, target_train)

    return model, data_test, target_test


@op(out={"model": Out(), "data_test": Out(), "target_test": Out()})
def create_model(data):
    '''Create fitted model'''

    model, features, target = load_model(data)
    model, data_test, target_test = fit_model(model, features, target)

    return model, data_test, target_test
