"""
a: zak-45
d: 03/12/2024
v: 1.0.0.0

 Tkinter info window

"""


import contextlib
import tkinter as tk
import sys

def show_message(message, msg_type: str = ''):
    """
    Create a Tkinter window to inform the user.

    This function initializes a Tkinter window with a message informing the user. It includes an 'OK' button
    to dismiss the message.
    """

    def on_close():
        """Linux/macOS-safe forced window close to ensure Tk mainloop exits.
                Safely closes and destroys a tkinter window or widget.
        Attempts to update, quit, and destroy the object, ignoring any exceptions that occur.

        """
        with contextlib.suppress(Exception):
            root.update_idletasks()
            root.update()
        with contextlib.suppress(Exception):
            root.quit()
        with contextlib.suppress(Exception):
            root.destroy()


    root = tk.Tk()
    root.title("WLEDInformation")
    root.protocol("WM_DELETE_WINDOW", on_close)


    bg_color = 'red' if msg_type == 'error' else '#0E7490'
    root.configure(bg=bg_color)  # Set the background color
    label = tk.Label(root, text=message, bg=bg_color, fg='white', justify=tk.LEFT, padx=5, pady=5, wraplength='360p')
    label.pack()

    # Create an OK button to close the window
    ok_button = tk.Button(root, text="OK", command=on_close)
    ok_button.pack(pady=10)

    # Make the window stay on top of other windows
    with contextlib.suppress(Exception):
        root.attributes('-topmost', True)

    if sys.platform.lower() == 'win32':
        root.attributes('-toolwindow', True)
    elif sys.platform.lower() == 'linux':
        root.attributes('-type', 'dialog')
        root.overrideredirect(False)
    elif sys.platform.lower() == 'darwin':
        root.attributes('-notify', True)
        root.attributes('-type', 'dialog')

    # Start the Tkinter event loop
    root.mainloop()
    on_close()

if __name__ == "__main__":

    if len(sys.argv) > 2:
        show_message(sys.argv[1], sys.argv[2])
    else:
        show_message('bad args number, need 2: message and "info" or "error" if want red bg', 'error')
