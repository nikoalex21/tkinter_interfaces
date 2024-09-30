import tkinter as tk 

ventana = tk.Tk()

ventana.title("mi primer ventana")
ventana.geometry("600x400") #se puede configurar para saber donde colocar la ventana
ventana.minsize(400, 200) #Ancho y alto minimos 
ventana.maxsize(800, 600)#maximo
ventana.iconbitmap("game.ico")
#cambiar color de fondo de la ventana
ventana.configure(bg="LightCyan2")
#se utiliza para configurar si la ventana se puede redimensionar
ventana.resizable(False,True) #ancho y alto
#agregar transparencia a la ventana(opcional) el valor va de 1 al 100%
ventana.attributes("-alpha", 0.0)



ventana.mainloop()