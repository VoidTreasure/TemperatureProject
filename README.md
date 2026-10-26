# Temperature Converter

A small Python project for converting temperatures between Celsius, Fahrenheit, and Kelvin.

## Features

The project includes four functions:

- `celsius_to_fahrenheit()` — converts Celsius to Fahrenheit.
- `fahrenheit_to_celsius()` — converts Fahrenheit to Celsius.
- `celsius_to_kelvin()` — converts Celsius to Kelvin and raises `ValueError` for temperatures below absolute zero.
- `kelvin_to_celsius()` — converts Kelvin to Celsius.

## Requirements

- Python 3.12 or a compatible Python version
- pytest

## Installation

Install the required package:

```bash
python -m pip install -r requirements.txt
```

## Running tests

Run the tests from the project directory:

```bash
python -m pytest -v
```

## GitHub Actions

The project uses GitHub Actions to run tests automatically on pushes and pull requests. The workflow can also be started manually using `workflow_dispatch`.

## Project structure

```text
TemperatureProject/
├── temperature.py
├── requirements.txt
├── tests/
│   └── test_temperature.py
└── .github/
    └── workflows/
        └── tests.yml
```