from tkinter import *
from tkinter import messagebox

def generate_fibonacci():
    """
    Generates the Fibonacci sequence based on the entered number of terms.
    Updates the output text box with the sequence (center-aligned).
    """
    try:
        no_of_terms = int(number_of_terms_entry.get())
        if no_of_terms <= 0:
            raise ValueError("Number of terms must be a positive integer.")
        
        output.delete(0.0, END)  # Clear the output text box

        # Fibonacci series generation logic
        a, b = 0, 1
        for i in range(no_of_terms):
            if i != no_of_terms - 1:
                output.insert(END, f"{a}, ", "center_tag")  # Print the term with center alignment tag
            else:
                output.insert(END, f"{a}", "center_tag")  # Print the last term with center alignment tag
            a, b = b, a + b

        # Configure the "center_tag" for center alignment (after generating the output)
        output.tag_configure("center_tag", justify=CENTER)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_all():
    """
    Clears all the input fields and output text box.
    """
    number_of_terms_entry.delete(0, END)
    output.delete(0.0, END)

# Create the main window
window = Tk()
window.title("FIBONACCI SERIES GENERATOR")
window.geometry('1325x660+0+0')

# Load and set the icon image
icon_image = PhotoImage(file="Image\icon.png")
window.iconphoto(True, icon_image)

# Set the background color
window.configure(bg='#EB9159')

# Labels
label1 = Label(window, text="WELCOME TO FIBONACCI SERIES GENERATOR", bg='#EB9159', fg='White', font=("Times New Roman bold", 28), height=3, width=55, wraplength=800)
label1.pack()

# Frame for centering label and entry
center_frame = Frame(window)
center_frame.pack()  # Pack the frame in the window

# Label for number of terms (within the center frame)
label3 = Label(center_frame, text="ENTER NUMBER OF TERMS:", bg='#F1F1F2', fg='#EB9159', font=("Times New Roman bold", 14), height=2, width=25)  # Adjust width if needed
label3.pack(side=LEFT)  # Place the label to the left within the frame

# Entry field for number of terms (within the center frame)
number_of_terms_entry = Entry(center_frame, width= 6 , fg='#EB9159', font=("Times New Roman bold", 14))
number_of_terms_entry.pack(side=LEFT, padx=16, pady=8)  # Place the entry to the left within the frame

# Frame to hold the buttons
button_frame = Frame(window, bg='#EB9159')
button_frame.pack()

# Button to generate the sequence
generate_button = Button(button_frame, text="GENERATE", command=generate_fibonacci, font=("Times New Roman bold", 14), bg='#F1F1F2', fg='#EB9159')
generate_button.pack(side=LEFT, padx=10, pady=16)

# Button to clear all fields
clear_button = Button(button_frame, text="CLEAR ALL", command=clear_all, font=("Times New Roman bold", 14), bg='#F1F1F2', fg='#EB9159')
clear_button.pack(side=LEFT, padx=10, pady=16)

# Text box to display the output
output_frame = Frame(window)
output_frame.pack()
output = Text(output_frame, bg='#F1F1F2', fg='#EB9159', font=("Times New Roman bold", 14), height=15, width=70, wrap=WORD)
output.pack(side=LEFT, expand=True, fill=BOTH)

# Load and resize the Definition.png image
definition_photo = PhotoImage(file='Image\Definition.png')
definition_photo = definition_photo.subsample(3)  # Resize the image

# Label for the Definition.png image
definition_label = Label(window, image=definition_photo, bg='#EB9159')
definition_label.place(relx=1.0, rely=0, anchor='ne')  # Position the image at the upper right corner

# Resize and place the Background_image.png at the bottom-right corner
background_photo = PhotoImage(file='Image\Background_image.png')
background_photo = background_photo.subsample(3)  # Resize the image
background_label = Label(window, image=background_photo, bg='#EB9159')
background_label.place(relx=1.0, rely=1.0, anchor='se')  # Position the image at the bottom-right corner

# Run the main loop
window.mainloop()
