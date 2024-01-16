import pytest
from python_pipeline_jenkins_learn.math_operations import add, sub, mul, div


def test_add():
    assert add(10, 2) == 12
    assert add(0, 5) == 5
    assert add(-10, 2) == -8


def test_sub():
    assert sub(10, 2) == 8
    assert sub(0, 5) == -5
    assert sub(-10, 2) == -12


def test_mul():
    assert mul(10, 2) == 20
    assert mul(0, 5) == 0
    assert mul(-10, 2) == -20


class TestMul:
    def test_div(self):
        assert div(10, 2) == 5
        assert div(0, 5) == 0
        assert div(-10, 2) == -5

    def test_div_by_zero(self):
        with pytest.raises(ValueError):
            div(10, 0)
