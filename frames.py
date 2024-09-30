import tkinter as tk
ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("600x400")
ventana.configure(bg="LightCyan2")

""" frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="blue", bd=5)

frame2=tk.Frame(frame1)
frame2.configure(width=200, height=150, bg="green", bd=5)

boton = tk.Button(frame1, text="Alex")

frame1.pack()
frame2.pack()
boton.pack() """

labelFrame= tk.LabelFrame(ventana,text="GRupo", bg="yellow", padx=10, pady=10)
labelFrame.configure(width=300, height=200)
labelFrame.pack()

ventana.mainloop()