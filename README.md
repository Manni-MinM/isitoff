# Is It Off? - Persian Holiday Checker

Is It Off? is a simple Python package designed to gather holiday information and identify holidays and off days in the Persian calendar. It uses an external endpoint to provide accurate holiday data, making it easy for developers to integrate Persian holiday information into their applications.

## Features

- **Off Day Identification**: Easily identify whether a specific date is a holiday or an off day.
- **Holiday Information**: Retrieve a list of holidays in the Persian calendar.
- **Jalali and Gregorian Date Conversion**: Convert between Jalali and Gregorian dates.
- **Simple Integration**: Easy to use and integrate into your Python applications.

## Installation

You can install Is It Off? from PyPI using pip:

```bash
pip install isitoff
```

## Usage

Here’s how to use the `Isitoff` class to get Jalali and Gregorian dates:

```python
from isitoff import Isitoff
import jdatetime
from datetime import datetime

# Create an instance of Isitoff
holiday_checker = Isitoff()

# Get Jalali date for a given Gregorian date
gregorian_date = datetime(2024, 9, 21)  # Example Gregorian date
jalali_date = holiday_checker.get_jalali(gregorian_date)
print(f"Jalali date: {jalali_date}")

# Convert a Gregorian date to a Jalali date
converted_jalali = holiday_checker.get_gregorian(gregorian_date)
print(f"Converted Jalali date: {converted_jalali}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
