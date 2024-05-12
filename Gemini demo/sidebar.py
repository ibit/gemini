import tkinter as tk

root = tk.Tk()

button1 = tk.Button(root,text="赤",bg="red")
button1.pack(fill="x")
button2 = tk.Button(root,text="青",bg="blue")
button2.pack(fill="x")
button3 = tk.Button(root,text="緑",bg="green")
button3.pack(fill="x")

root.mainloop()