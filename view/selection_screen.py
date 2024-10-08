import tkinter as tk
import view.helper as helper
import view.consts as consts
import view.option_screens as options

# Function to show the main selection screen
def show_selection_screen(root):
    helper.clear_frame(root)

    # Title label
    label = tk.Label(root, text="Triangle Manager", font=(consts.DEFAULT_SCREEN_FONT, 18))
    label.pack(pady=20)

    # Subtitle label
    subtitle = tk.Label(root, text="Choose a method to create a triangle:", font=(consts.DEFAULT_SCREEN_FONT, 14))
    subtitle.pack(pady=10)

    # Option 1 button (From three sides)
    option1_button = tk.Button(root, text="Option 1 (From three sides)", width=40, command=lambda: options.show_option1_screen(root))
    option1_button.pack(pady=10)

    # Option 2 button (From three angles)
    option2_button = tk.Button(root, text="Option 2 (From three angles)", width=40, command=lambda: options.show_option2_screen(root))
    option2_button.pack(pady=10)

    # Option 3 button (From two side lengths and one angle)
    option3_button = tk.Button(root, text="Option 3 (From two side lengths and one angle)", width=40, command=lambda: options.show_option3_screen(root))
    option3_button.pack(pady=10)
