import tkinter as tk

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes
canvas = tk.Canvas(frame)
canvas.create_rectangle(10, 50, 20, 60, outline="#1abc9c", fill="#FF0000")
canvas.create_oval(500, 500, 550, 550, outline="#1abc9c", fill="#000000")
canvas.create_text(200, 200, text="Just do it", font=("Purisa", 26))
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()

