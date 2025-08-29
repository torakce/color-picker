import tkinter as tk
from tkinter import colorchooser
import colorsys

def rgb_to_hsv(r: int, g: int, b: int):
    """Convert RGB values (0-255) to HSV (values between 0 and 1).

    Returns a tuple of (h, s, v).
    """
    return colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)


def add_to_history(history, color, limit=10):
    """Add a color to the beginning of the history list.

    Ensures the history does not grow beyond ``limit`` items.
    Returns the new history list.
    """
    return [color] + history[: limit - 1]

def main():
    root = tk.Tk()
    root.title("Color Picker")

    hex_var = tk.StringVar()
    rgb_var = tk.StringVar()
    hsv_var = tk.StringVar()

    color_history = []
    history_listbox = tk.Listbox(root, height=10)

    def copy_rgb():
        text = rgb_var.get()
        if text:
            root.clipboard_clear()
            root.clipboard_append(text)
            root.update()

    def pick_color():
        nonlocal color_history
        result = colorchooser.askcolor()
        if not result or not result[0]:
            return
        (r, g, b) = [int(v) for v in result[0]]
        h, s, v = rgb_to_hsv(r, g, b)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"

        hex_var.set(hex_color)
        rgb_var.set(f"{r}, {g}, {b}")
        hsv_var.set(f"{h:.3f}, {s:.3f}, {v:.3f}")

        root.clipboard_clear()
        root.clipboard_append(hex_color)
        root.update()

        color_history = add_to_history(color_history, hex_color)
        history_listbox.delete(0, tk.END)
        for c in color_history:
            history_listbox.insert(tk.END, c)

    tk.Button(root, text="Pick color", command=pick_color).pack(pady=10)

    tk.Label(root, text="HEX:").pack()
    tk.Label(root, textvariable=hex_var).pack()

    tk.Label(root, text="RGB:").pack()
    tk.Label(root, textvariable=rgb_var).pack()
    tk.Button(root, text="Copy RGB", command=copy_rgb).pack(pady=5)

    tk.Label(root, text="HSV:").pack()
    tk.Label(root, textvariable=hsv_var).pack()

    tk.Label(root, text="History:").pack()
    history_listbox.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
