import pytest

from src.square import Square
from src.rectangle import Rectangle


@pytest.fixture
def square():
    return Square(10)


def test_square_area(square):

    assert square.area == 100


def test_square_perimeter(square):

    assert square.perimeter == 40


def test_square_add_area(square):

    rectangle = Rectangle(3, 5)

    assert square.add_area(rectangle) == 115


def test_square_negative_side():

    with pytest.raises(ValueError):

        Square(-1)


def test_square_zero_side():

    with pytest.raises(ValueError):

        Square(0)
