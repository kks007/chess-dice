import tkinter as tk
import random

def run_code():
    output = random.choices(my_list, k=n)
    clear_output_boxes()
    for i, element in enumerate(output):
        output_boxes[i].insert(tk.END, element)
        output_boxes[i].tag_configure("center", justify='center')  # Configure the tag for center alignment
        output_boxes[i].tag_add("center", "1.0", "end")  # Apply the center alignment tag to the entire text

def clear_output_boxes():
    for box in output_boxes:
        box.delete(1.0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Chess Dice")
window.geometry("400x300") 

my_list = ['King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn']
n = 3


# Create text boxes to display the output
output_boxes = []
for _ in range(n):
    output_box = tk.Text(window, height=2, width=15, padx=5, pady=5) 
    output_box.pack(padx=10, pady=10)  
    output_box.configure(font=("Arial", 12))  
    output_boxes.append(output_box)

# trigger button
button = tk.Button(window, text="Roll Dice", command=run_code, height=2, width=15)  # Increase button size
button.pack(pady=20)  # Double the top padding

# Run the GUI event loop
window.mainloop()
