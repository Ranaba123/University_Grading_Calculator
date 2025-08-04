# Grading Calculator

## Overview
The Grading Calculator is a Python application designed to process student credit data, determine academic outcomes based on predefined criteria, and visualize the results in a histogram. It allows users to input pass, defer, and fail credits, validates the input, categorizes the outcomes (Progress, Progress (module trailer), Module Retriever, or Exclude), and generates a graphical representation of the results. Additionally, it supports saving the results to a text file for record-keeping.

## Features
- **Input Validation**: Ensures that credit inputs are integers and within the valid range (0, 20, 40, 60, 80, 100, 120).
- **Outcome Determination**: Categorizes student outcomes based on credit inputs:
  - **Progress**: 120 pass credits.
  - **Progress (module trailer)**: 100 pass credits with 20 defer or fail credits.
  - **Exclude**: 80, 100, or 120 fail credits.
  - **Module Retriever**: All other valid cases.
- **Histogram Visualization**: Displays a graphical histogram of outcomes using the `graphics` library, with bars for Progress, Trailer, Retriever, and Exclude categories.
- **Data Persistence**: Saves results to a timestamped text file in the format `YYYY_MM_DD_HH_MM.txt`.
- **User Interaction**: Allows multiple data entries in a session and provides the option to continue or quit.

## Requirements
- Python 3.x
- `graphics.py` library (for histogram visualization)

## Installation
1. Ensure Python 3.x is installed on your system.
2. Download and install the `graphics.py` library:
   - Download `graphics.py` from a reliable source (e.g., http://mcsp.wartburg.edu/zelle/python/).
   - Place `graphics.py` in the same directory as the script or in your Python path.
3. Save the provided Python script as `grading_calculator.py`.

## Usage
1. Run the script using Python:
   ```bash
   python grading_calculator.py
   ```
2. Follow the prompts to input credits for pass, defer, and fail categories.
3. The program validates inputs and displays the outcome for each set of credits.
4. Choose to continue entering data (`y`) or quit to view results (`q`).
5. Upon quitting, a histogram displays the distribution of outcomes, and results are saved to a timestamped text file.

## Example Interaction
```
************************************************************************University Grading Calculator*****************************************************************



Please enter your credits at pass: 100
Please enter your credits at defer: 20
Please enter your credits at fail: 0
Progress (module trailer)

Would you like to enter another data set?
Enter 'y' for yes or 'q' to quit and view results: q
```

- A histogram window will appear showing the outcome distribution.
- A file (e.g., `2025_08_04_10_46.txt`) will be created with the results.

## Code Structure
- **Main Function**: Orchestrates the program flow, including input collection, outcome determination, and histogram display.
- **Input Grading Function**: Validates and collects credit inputs.
- **Histogram Function**: Generates a graphical representation of outcomes using `graphics.py`.
- **Exception Handling**: Custom `Invalidrange` exception for out-of-range inputs and built-in `ValueError` for non-integer inputs.
- **Data Storage**: Uses a list to store outcomes and writes them to a file when the program exits.

## Notes
- The total credits (pass + defer + fail) must equal 120; otherwise, the input is rejected, and the user can retry or quit.
- The histogram scales vertically based on the count of each outcome (10 pixels per outcome).
- The text file is created with a timestamp to avoid overwriting previous results.

## Limitations
- Requires the `graphics.py` library for histogram visualization, which may not be compatible with all environments.
- No support for non-integer or negative credit inputs beyond the specified range.
- The histogram window must be closed manually to exit the program.

## License
This project is provided as-is for educational purposes. No official license is specified.
