
import pytest

from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
)


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize(
    "fahrenheit, expected",
    [
        (32, 0),
        (212, 100),
        (-40, -40),
    ],
)
def test_fahrenheit_to_celsius(fahrenheit, expected):
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(expected)


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == pytest.approx(273.15)


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == pytest.approx(0)

def celsius_to_kelvin(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Температура не може бути нижче абсолютного нуля")
    return celsius + 273.15