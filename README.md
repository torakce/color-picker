# Color Picker

Simple cross-platform color picker built with Python and Tkinter.

## Requirements

- Python 3

## Usage

```bash
python app.py
```

Click **Pick color** to choose a color. The HEX, RGB and HSV values are displayed and the HEX code is copied to the clipboard.
Each picked color is stored in a history list and can be revisited later.
Use the **Copy RGB** button to copy the RGB value to the clipboard.

## Tests

```bash
python -m unittest
```

## Packaging

Use [PyInstaller](https://pyinstaller.org/) to build standalone executables for
Windows and macOS.

### Windows

```bash
pip install pyinstaller
pyinstaller color_picker.spec
```

### macOS

```bash
pip install pyinstaller
pyinstaller color_picker.spec
```

The binaries will be available in the `dist/` directory once the build
completes.
