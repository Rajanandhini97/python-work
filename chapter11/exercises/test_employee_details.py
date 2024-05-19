import pytest
from employee import Employee


@pytest.fixture
def employee_detail():
    """Employee detail that will be available to all test functions"""
    employee_one = Employee('Nash', 'Willie', 100000)
    return employee_one


def test_give_default_raise(employee_detail):
    """Test the default amount"""
    employee_detail.give_raise()

    assert employee_detail.salary == 150000


def test_give_custom_raise(employee_detail):
    """Test give raise by providing custom amount"""
    employee_detail.give_raise(20000)

    assert employee_detail.salary == 120000