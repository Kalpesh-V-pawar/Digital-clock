import tkinter as tk
from time import strftime

def digital_clock():
    # Update the time on the label every second
    current_time = strftime("%H:%M:%S %p")  # Format: HH:MM:SS AM/PM
    label.config(text=current_time)
    label.after(1000, digital_clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x200")
window.configure(bg="black")

# Create a label for the clock
label = tk.Label(
    window,
    font=("Arial", 50, "bold"),
    background="black",
    foreground="cyan"
)
label.pack(anchor="center")

# Start the clock
digital_clock()

# Run the application
window.mainloop()
