import pytest

from src.rectangle import Rectangle
from src.square import Square


@pytest.fixture
def rectangle():
    return Rectangle(3, 5)


def test_rectangle_area(rectangle):

    assert rectangle.area == 15


def test_rectangle_perimeter(rectangle):

    assert rectangle.perimeter == 16


def test_rectangle_add_area(rectangle):

    square = Square(10)

    assert rectangle.add_area(square) == 115


def test_rectangle_negative_side():

    with pytest.raises(ValueError):

        Rectangle(-1, 5)


def test_rectangle_zero_side():

    with pytest.raises(ValueError):

        Rectangle(0, 5)


def test_rectangle_add_area_wrong_type(rectangle):

    with pytest.raises(ValueError):

        rectangle.add_area("hello")