import pytest
from employee import Employee

@pytest.fixture
def employee_response():
    test_employee = Employee('morgan', 'arthur', 10000)
    return test_employee

def test_default_raise(employee_response):
    employee_response.give_raise()
    assert employee_response.salary == 15000

def test_custom_raise(employee_response):
    employee_response.give_raise(raise_salary=10000)
    assert employee_response.salary == 20000