# Keyboard Tester

This is a Python script to test keyboard inputs. It tracks the number of times each key is pressed and displays the counts. The script uses the `keyboard` module to hook into keyboard events and keeps a running count of key presses.

## Prerequisites

- Python 3.x
- `keyboard` module
- `time` module (part of the Python Standard Library)

You can install the `keyboard` module using pip:

```bash
pip install keyboard
```

## Script Overview

The script initializes a dictionary to keep track of key counts and defines a function to handle key events. It then registers an event listener to hook into keyboard events

## How to Run

1. Make sure you have installed the required modules.
2. Save the script to a file, for example `keyboard_tester.py`.
3. Run the script:

    ```bash
    python keyboard_tester.py
    ```

4. Press any keys on your keyboard. The script will display the counts of key presses every second.
5. Press the `Esc` key to exit the script and see the final counts.


## Example Output

```css
Press 'Esc' to exit and get the final results.
Key Counts: {}
Key Counts: {'a': 1}
Key Counts: {'a': 1, 'b': 2}
Key Counts: {'a': 1, 'b': 2, 'c': 3}
...
Final Key Counts: {'a': 1, 'b': 2, 'c': 3}
```
## Notes

- The script runs indefinitely until the `Esc` key is pressed.
- If you need to stop the script without pressing `Esc`, you can use `
