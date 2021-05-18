import pandas as pd
from tests.helper import Helper
from pyaugmecon.pyaugmecon import PyAugmecon
from tests.optimization_models import four_kp_model

model_type = '4kp50'

options = {
    'name': model_type,
    'grid_points': 53,
    'nadir_points': [718, 717, 705],
    }

py_augmecon = PyAugmecon(four_kp_model(model_type), options)
py_augmecon.solve()

xlsx = pd.ExcelFile(f'tests/input/{model_type}.xlsx', engine='openpyxl')


def test_payoff_table():
    payoff_table = Helper.read_excel(xlsx, 'payoff_table').to_numpy()
    assert Helper.array_equal(py_augmecon.payoff_table, payoff_table, 2)


def test_e_points():
    e_points = Helper.read_excel(xlsx, 'e_points').to_numpy()
    assert Helper.array_equal(py_augmecon.e, e_points, 2)


def test_pareto_sols():
    pareto_sols = Helper.read_excel(xlsx, 'pareto_sols').to_numpy()
    assert Helper.array_equal(py_augmecon.pareto_sols, pareto_sols, 2)
