import pytest
from math import pi

from src.circle import Circle
from src.square import Square


@pytest.fixture
def circle():
    return Circle(10)


def test_circle_area(circle):

    assert circle.area == pi * 100


def test_circle_perimeter(circle):

    assert circle.perimeter == 2 * pi * 10


def test_circle_add_area(circle):

    square = Square(10)

    assert circle.add_area(square) == circle.area + square.area


def test_circle_negative_radius():

    with pytest.raises(ValueError):

        Circle(-1)


def test_circle_zero_radius():

    with pytest.raises(ValueError):

        Circle(0)