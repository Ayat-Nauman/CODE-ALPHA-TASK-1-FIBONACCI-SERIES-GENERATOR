from tkinter import *

def generate_fibonacci():
  """
  Generates the Fibonacci sequence based on the entered number of terms.
  Updates the output text box with the sequence.
  """
  no_of_terms = int(number_of_terms_entry.get())
  output.delete(0.0, END)  # Clear the output text box

  a, b = 0, 1
  output_string = f"1, "
  for i in range(1, no_of_terms):
    c = a + b
    output_string += f"  {c}," if i != no_of_terms - 1 else f"  {c}"
    a, b = b, c
  output.insert(END, output_string)

# Create the main window
window = Tk()
window.title("Fibonacci Series Generator")
window.geometry('550x400+400+200')

# Background color (adjust to your preference)
window.configure(bg='#F0F8FF')

# Professional font (replace with your preferred option)
pro_font = ("Arial", 12, "bold")

# Labels
label1 = Label(window, text="FIBONACCI SERIES GENERATOR", bg=window.cget('bg'), fg='#1E90FF', font=pro_font)
label1.pack()

label2 = Label(window, text="""The Fibonacci Sequence is a series where each number is the sum of the two preceding numbers. 
This sequence has many applications in mathematics, computer science, and nature.""", bg=window.cget('bg'), fg='#1E90FF', font=pro_font, wraplength=900)
label2.pack(pady=10)

# Frame to hold the label and entry widgets (inherit background color)
label_and_entry_frame = Frame(window, bg=window.cget('bg'))
label_and_entry_frame.pack(pady=20)

# Label for number of terms with a dark blue background and white text
label3 = Label(label_and_entry_frame, text="ENTER NUMBER OF TERMS:", bg='#1E90FF', fg='white', font=pro_font)
label3.pack(side=LEFT)

# Entry field for number of terms (reduced width)
number_of_terms_entry = Entry(label_and_entry_frame, width=4, fg='black', font=pro_font)
number_of_terms_entry.pack(side=LEFT, padx=8, pady=4)

# Generate button below the entry field
generate_button = Button(window, text="GENERATE", command=generate_fibonacci, font=pro_font, bg='#1E90FF', fg='white', width=12)
generate_button.pack(pady=10, after=label_and_entry_frame)

# Text box with a light gray background, black text, and increased width
output = Text(window, bg='#DFDFDF', fg='black', font=pro_font, height=15, width=60)
output.pack()
output.config(relief=SUNKEN)  # Add a border to the text box

# Run the main loop
window.mainloop()
