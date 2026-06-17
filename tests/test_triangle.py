import pytest

from src.triangle import Triangle
from src.square import Square


@pytest.fixture
def triangle():
    return Triangle(13, 14, 15)


def test_triangle_area(triangle):

    assert triangle.area == 84


def test_triangle_perimeter(triangle):

    assert triangle.perimeter == 42


def test_triangle_add_area(triangle):

    square = Square(10)

    assert triangle.add_area(square) == 184


def test_triangle_negative_side():

    with pytest.raises(ValueError):

        Triangle(-1, 2, 3)


def test_triangle_zero_side():

    with pytest.raises(ValueError):

        Triangle(0, 2, 3)


def test_triangle_invalid_sides():

    with pytest.raises(ValueError):

        Triangle(1, 2, 10)