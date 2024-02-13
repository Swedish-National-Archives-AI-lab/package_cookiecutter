import pytest

from {{cookiecutter.package_name}}.main import add, subtract, gpu_intensive_calculation


def test_add() -> None:
    assert add(1, 2) == 3


def test_subtract() -> None:
    assert subtract(2, 1) == 1


@pytest.mark.gpu
def test_gpu_intensive_calculation() -> None:
    x = 4
    expected_result = 16
    assert gpu_intensive_calculation(x) == expected_result, "The GPU intensive calculation did not produce the expected result"