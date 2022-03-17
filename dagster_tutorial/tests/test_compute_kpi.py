'''Test compute kpi
'''
import unittest
from compute_kpi import find_highest_calorie_cereal


def test_find_highest_calorie_cereal():
    '''Test for find_highest_calorie_cereal'''

    cereals = [
        {"name": "hi-cal cereal", "calories": 400},
        {"name": "lo-cal cereal", "calories": 50},
    ]

    computed = find_highest_calorie_cereal(cereals)
    expected = "hi-cal cereal"

    unittest.TestCase().assertEqual(expected, computed)
