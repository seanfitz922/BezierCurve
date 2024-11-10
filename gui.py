import tkinter as tk
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
from bezier import main

# Initialize the main application window
root = tk.Tk()
root.title("Bézier Cubit")
root.geometry("400x300")
root.configure(bg="#f0f0f5")  # Light background color

# Set a custom font for buttons and labels
# https://www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/
title_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(family="Helvetica", size=12)
text_font = font.Font(family="Helvetica", size=14)


# https://www.tutorialspoint.com/getting-every-child-widget-of-a-tkinter-window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Load the home icon image
def get_home_icon():
    icon = Image.open("simple_house.jpg")
    icon = icon.resize((30, 30), Image.LANCZOS)  # Resize if necessary
    return ImageTk.PhotoImage(icon)

# return to the homescreen
def show_home_screen():
    clear_window()
    root.configure(bg="#f0f0f5")

    # Create a frame for the title
    # https://www.geeksforgeeks.org/python-tkinter-frame-widget/
    title_frame = tk.Frame(root, bg="#3b5998", padx=10, pady=10)
    title_frame.pack(fill="x", pady=(0, 20))

    title_label = tk.Label(title_frame, text="Bézier Cubit", font=title_font, fg="white", bg="#3b5998")
    title_label.pack()
    
    # Place buttons inside another frame 
    button_frame = tk.Frame(root, bg="#f0f0f5")
    button_frame.pack()

    # Create and grid the buttons
    # https://www.pythontutorial.net/tkinter/tkinter-grid/
    button_input_points = tk.Button(button_frame, text="Input Points", font=button_font, width=15, height=2,
                                    bg="#4CAF50", fg="white", command=input_points_menu)
    button_input_points.grid(row=0, column=0, pady=10)

    button_free_hand = tk.Button(button_frame, text="Free Hand", font=button_font, width=15, height=2,
                                bg="#2196F3", fg="white", command=free_hand)
    button_free_hand.grid(row=1, column=0, pady=10)

    button_examples = tk.Button(button_frame, text="Examples", font=button_font, width=15, height=2,
                                bg="#FF5722", fg="white", command=examples)
    button_examples.grid(row=2, column=0, pady=10)

# Create a function for each button ADD FUINCTIONALITY
def input_points_menu():

    # clsoe previous windows
    clear_window()

    # https://www.pythontutorial.net/tkinter/tkinter-toplevel/
    # Create a new top-level window
    # input_window = tk.Toplevel(root)
    # input_window.title("Input Points")
    # input_window.geometry("400x300")
    root.configure(bg="#e0e0eb")

    # Label for entering points
    input_label = tk.Label(root, text="Enter Points:", font=title_font, bg="#e0e0eb")
    input_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx = 10, pady=(10, 10)) 

    # P1 label and entry
    point_one_label = tk.Label(root, text="P1:", font = text_font,  bg="#e0e0eb")
    point_one_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    point_one_entry = tk.Entry(root, width=10)
    point_one_entry.grid(row=1, column=1, pady=5, ipadx = 15)

    # formatting rules
    point_one_example = tk.Label(root, text="Format: (x,y)", font=text_font, bg="#e0e0eb")
    point_one_example.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    # P2 label and entry
    point_two_label = tk.Label(root, text="P2:", font = text_font, bg="#e0e0eb")
    point_two_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    point_two_entry = tk.Entry(root, width=10)
    point_two_entry.grid(row=2, column=1, pady=5, ipadx = 15)

    # formatting rules
    point_two_example = tk.Label(root, text="- Only integers", font=text_font, bg="#e0e0eb")
    point_two_example.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    # P3 label and entry
    point_three_label = tk.Label(root, text="P3:", font = text_font, bg="#e0e0eb")
    point_three_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    point_three_entry = tk.Entry(root, width=10)
    point_three_entry.grid(row=3, column=1, pady=5, ipadx = 15)

    # formatting rules
    point_three_example = tk.Label(root, text="- Must enter four points", font=text_font, bg="#e0e0eb")
    point_three_example.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    # P4 label and entry
    point_four_label = tk.Label(root, text="P4:", font = text_font, bg="#e0e0eb")
    point_four_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    point_four_entry = tk.Entry(root, width=10)
    point_four_entry.grid(row=4, column=1, pady=5, ipadx = 15)

    # Submit button
    # https://stackoverflow.com/questions/51686567/making-a-new-window-with-an-input-widget-using-tkinter
    # Assuming `control_points` is a predefined list to store the points
    draw_button = tk.Button(root, text="Draw Curve", font=button_font, width=15, height=2, bg="#4CAF50", fg="white",
                        command=lambda: parse_points_string([
                            (point_one_entry.get()), (point_two_entry.get()),
                            (point_three_entry.get()), (point_four_entry.get())
                        ]))
    
    draw_button.grid(row=5, column=0, columnspan=2, pady=15, padx=10)

    home_icon = get_home_icon()
    home_button = tk.Button(root, image=home_icon, font=button_font, borderwidth=0,
              command=show_home_screen)
    
    home_button.image = home_icon 
    
    home_button.grid(row=0, column=2, columnspan=2, pady=15, padx=10, sticky="e")

def parse_points_string(points_list):
    gui_points = []
    # Flag to track if all inputs are valid
    valid_input = True  

    for point_str in points_list:
        points = point_str.split(",")
        
        # Ensure length
        if len(points) == 2:
            try:
                # Convert to integers and append as a tuple
                gui_points.append((int(points[0].strip()), int(points[1].strip())))
            except ValueError:
                # Show error message for invalid integer conversion
                messagebox.showerror("Input Error", f"Invalid input: '{point_str}'. Please enter valid integers.")
                # Mark as invalid input
                valid_input = False  
                break
        else:
            messagebox.showerror("Input Error", "Invalid input length. Please enter two integers for each field.")
            valid_input = False  
            break

    # Pass list of points to main to draw only if input is valid
    if valid_input:
        main(gui_points)

# call main to run free hand mode
def free_hand():
    main()

def examples():
    clear_window()
    root.configure(bg="#e0e0eb")

    # Example label
    example_label = tk.Label(root, text="Example Point Entries:", font=title_font, bg="#e0e0eb")
    example_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 10)) 

    # Example 1 label
    example_one_label = tk.Label(root, text="Example 1:", font=text_font, bg="#e0e0eb")
    example_one_label.grid(row=1, column=0, padx=10, sticky="w")

    # Draw Example One button
    draw_example_one_button = tk.Button(root, text="Draw Curve", font=button_font, bg="#4CAF50", fg="white",
                        command=lambda: main([
                            (0, 0), (500, 500), (700, 1000), (1000, 1000)
                        ]))
    # Align left
    draw_example_one_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")  

    # Example 2 label
    example_two_label = tk.Label(root, text="Example 2:", font=text_font, bg="#e0e0eb")
    example_two_label.grid(row=3, column=0, padx=10, sticky="w")

    # Draw Example Two button
    draw_example_two_button = tk.Button(root, text="Draw Curve", font=button_font, bg="#4CAF50", fg="white",
                        command=lambda: main([
                            (0, 1080), (1920, 0), (0, 0), (1920, 1080)
                        ]))
    # Align left
    draw_example_two_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    # Example 3 label
    example_three_label = tk.Label(root, text="Example 3:", font=text_font, bg="#e0e0eb")
    example_three_label.grid(row=5, column=0, padx=10, sticky="w")

    # Draw Example Three button
    draw_example_three_button = tk.Button(root, text="Draw Curve", font=button_font, bg="#4CAF50", fg="white",
                        command=lambda: main([
                            (270, 820), (570, 180), (1400, 200), (1600, 820)
                        ]))
    # Align left
    draw_example_three_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")    

    home_icon = get_home_icon()
    home_button = tk.Button(root, image=home_icon, font=button_font, borderwidth=0,
              command=show_home_screen)
    
    home_button.image = home_icon 
    
    home_button.grid(row=0, column=2, columnspan=2, pady=15, padx=65, sticky="e")


# Run the initial home screen
show_home_screen()

# Run the main event loop
root.mainloop()