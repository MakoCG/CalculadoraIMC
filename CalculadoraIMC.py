from tkinter import *
from tkinter import messagebox

class Inicio:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calcualdora de índice de masa corporal")
        self.ventana.geometry("500x750") 
        self.ventana.resizable(0,0)
        self.peso = StringVar()
        self.estatura = StringVar()
        self.IMC = StringVar()
        self.estado = StringVar()
        self.label_estado = Label()

    def construir(self):
        marco_titulo = Frame(self.ventana, width=250, height=50)
        marco_titulo.propagate(False)
        marco_titulo.pack(fill=X, expand=True, side=TOP, anchor=N)

        titulo = Label(marco_titulo, text="Calculo de IMC", padx=10, pady=10, fg="#d7fbe8", bg="#1fab89", font=("Cooper Black",40))
        titulo.pack(fill=X, expand=True, side=TOP, anchor=N)

        marco_datos = Frame(self.ventana, width=250, height=400, padx=20)
        marco_datos.propagate(False)
        marco_datos.pack(fill=X, expand=True, side=TOP, anchor=N)

        label_peso = Label(marco_datos, text="Peso (en kilos)", pady=20, padx=20, fg="#62d2a2", font=("Verdana",30))
        label_peso.pack(side=TOP, anchor=W)

        peso_txt = Entry(marco_datos,textvariable=self.peso, font=("Verdana",20))
        peso_txt.pack(side=TOP, padx=10, pady=10)

        label_estatura = Label(marco_datos, text="Estatura (en metros)", padx=20, pady=20, fg="#62d2a2", font=("Verdana", 30))
        label_estatura.pack(side=TOP, anchor=W)

        estatura_txt = Entry(marco_datos,textvariable=self.estatura, font=("Verdana",20))
        estatura_txt.pack(side=TOP, padx=10, pady=10)

        marco_boton = Frame(self.ventana, width=250, height=100, padx=20)
        marco_boton.propagate(False)
        marco_boton.pack(fill=X, expand=True, side=TOP, anchor=N)

        boton_calculo = Button(marco_boton, text="Calcular", font=("Verdana",20), bg="#9df3c4", fg="#1fab89", padx=20, pady=20, command=self.ejecutar)
        boton_calculo.pack(side=TOP, anchor=N)

        marco_resultado = Frame(self.ventana, width=250, height=200, padx=20)
        marco_resultado.propagate(False)
        marco_resultado.pack(fill=X, expand=True, side=TOP, anchor=N)

        titulo_resultado = Label(marco_resultado, text="Resultado", font=("Verdana",20), fg="#62d2a2", padx=20, pady=20)
        titulo_resultado.pack(side=TOP, anchor=S)

        label_resultado = Label(marco_resultado, textvariable=self.IMC, font=("Verdana",20), fg="#62d2a2", padx=20, pady=20)
        label_resultado.pack(side=TOP, anchor=S)

        self.label_estado = Label(marco_resultado, textvariable=self.estado, font=("Verdana", 20), padx=20, pady=20)
        self.label_estado.pack(side=TOP, anchor=S)

    def ejecutar(self):
        try:
            valor_peso = float(self.peso.get())
            valor_estatura = float(self.estatura.get())
            self.IMC.set(round(valor_peso/(valor_estatura*valor_estatura),1))
            if valor_peso/(valor_estatura*valor_estatura) < 18.5:
                self.estado.set("Bajo Peso")
            elif valor_peso/(valor_estatura*valor_estatura) >= 18.5 and valor_peso/(valor_estatura*valor_estatura) <= 24.9:
                self.estado.set("Normopeso")
            elif valor_peso/(valor_estatura*valor_estatura) >= 25 and valor_peso/(valor_estatura*valor_estatura) <= 26.9:
                self.estado.set("Sobrepeso grado I")
            elif valor_peso/(valor_estatura*valor_estatura) >= 27 and valor_peso/(valor_estatura*valor_estatura) <= 29.9:
                self.estado.set("Sobrepeso grado II")
            elif valor_peso/(valor_estatura*valor_estatura) >= 30 and valor_peso/(valor_estatura*valor_estatura) <= 34.9:
                self.estado.set("Obesidad de tipo I")
            elif valor_peso/(valor_estatura*valor_estatura) >= 35 and valor_peso/(valor_estatura*valor_estatura) <= 39.9:
                self.estado.set("Obesidad de tipo II")
            elif valor_peso/(valor_estatura*valor_estatura) >= 40 and valor_peso/(valor_estatura*valor_estatura) <= 49.9:
                self.estado.set("Obesidad de tipo III (Mórbida)")
            elif valor_peso/(valor_estatura*valor_estatura) > 50:
                self.estado.set("Obesidad de tipo IV (extrema)")
            if self.estado.get() == "Bajo Peso":
                self.label_estado.config(fg="#aee6e6")
            elif self.estado.get() == "Normopeso":
                self.label_estado.config(fg="#3A8F1E")
            elif self.estado.get() == "Sobrepeso grado I":
                self.label_estado.config(fg="#ffa45b")
            elif self.estado.get() == "Sobrepeso grado II":
                self.label_estado.config(fg="#ec5858")
            elif self.estado.get() == "Obesidad de tipo I":
                self.label_estado.config(fg="#FF82ED")
            elif self.estado.get() == "Obesidad de tipo II":
                self.label_estado.config(fg="#30475e")
            elif self.estado.get() == "Obesidad de tipo III":
                self.label_estado.config(fg="#8F2C81")
            elif self.estado.get() == "Obesidad de tipo IV":
                self.label_estado.config(fg="#000000")
        except Exception as e:
            messagebox.showwarning("Error en el programa", e)

    def mostrar(self):
        self.ventana.mainloop()

inicio = Inicio()
inicio.construir()
inicio.mostrar()
