import tkinter as tk
from tkinter import font

# Initialize the main application window
root = tk.Tk()
root.title("Bezier Cubit")
root.geometry("400x300")
root.configure(bg="#f0f0f5")  # Light background color

# Set a custom font for buttons and labels
# https://www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/
title_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(family="Helvetica", size=12)

# Create a frame for the title
# https://www.geeksforgeeks.org/python-tkinter-frame-widget/
title_frame = tk.Frame(root, bg="#3b5998", padx=10, pady=10)
title_frame.pack(fill="x", pady=(0, 20))

title_label = tk.Label(title_frame, text="Bezier Cubit", font=title_font, fg="white", bg="#3b5998")
title_label.pack()

# Create a function for each button ADD FUINCTIONALITY
def open_input_points_menu():

    # define control points list
    control_points = []

    # https://www.pythontutorial.net/tkinter/tkinter-toplevel/
    # Create a new top-level window
    input_window = tk.Toplevel(root)
    input_window.title("Input Points")
    input_window.geometry("350x300")
    input_window.configure(bg="#e0e0eb")


    # Label for entering points
    input_label = tk.Label(input_window, text="Enter Points:", font=button_font, bg="#e0e0eb")
    input_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))

    # P1 label and entry
    point_one_label = tk.Label(input_window, text="P1:", bg="#e0e0eb")
    point_one_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    point_one_entry = tk.Entry(input_window, width=10)
    point_one_entry.grid(row=1, column=1, pady=5)

    # P2 label and entry
    point_two_label = tk.Label(input_window, text="P2:", bg="#e0e0eb")
    point_two_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    point_two_entry = tk.Entry(input_window, width=10)
    point_two_entry.grid(row=2, column=1, pady=5)

    # P3 label and entry
    point_three_label = tk.Label(input_window, text="P3:", bg="#e0e0eb")
    point_three_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    point_three_entry = tk.Entry(input_window, width=10)
    point_three_entry.grid(row=3, column=1, pady=5)

    # P4 label and entry
    point_four_label = tk.Label(input_window, text="P4:", bg="#e0e0eb")
    point_four_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    point_four_entry = tk.Entry(input_window, width=10)
    point_four_entry.grid(row=4, column=1, pady=5)

    # Submit button
    # https://stackoverflow.com/questions/51686567/making-a-new-window-with-an-input-widget-using-tkinter
    # Assuming `control_points` is a predefined list to store the points
    draw_button = tk.Button(input_window, text="Draw Curve", font=button_font, bg="#4CAF50", fg="white",
                            command=lambda: control_points.append((
                                point_one_entry.get(), 
                                point_two_entry.get(), 
                                point_three_entry.get(), 
                                point_four_entry.get()
                            )))
    
    draw_button.grid(row=5, column=0, columnspan=2, pady=15)


    # Close button
    close_button = tk.Button(input_window, text="Close", font=button_font, bg="#FF5722", fg="white",
                             command=input_window.destroy)
    close_button.grid(row=6, column=0, columnspan=2, pady=5)

    print("Input Points button clicked")

def free_hand():
    print("Free Hand button clicked")

def examples():
    print("Examples button clicked")

# Place buttons inside another frame for better organization
button_frame = tk.Frame(root, bg="#f0f0f5")
button_frame.pack()

# Create and grid the buttons
# https://www.pythontutorial.net/tkinter/tkinter-grid/
button_input_points = tk.Button(button_frame, text="Input Points", font=button_font, width=15, height=2,
                                bg="#4CAF50", fg="white", command=open_input_points_menu)
button_input_points.grid(row=0, column=0, pady=10)

button_free_hand = tk.Button(button_frame, text="Free Hand", font=button_font, width=15, height=2,
                             bg="#2196F3", fg="white", command=free_hand)
button_free_hand.grid(row=1, column=0, pady=10)

button_examples = tk.Button(button_frame, text="Examples", font=button_font, width=15, height=2,
                            bg="#FF5722", fg="white", command=examples)
button_examples.grid(row=2, column=0, pady=10)

# Run the main event loop
root.mainloop()
