import random
import tkinter as tk

ventana = tk.Tk()
ventana.title("SISTEMA DE DIAGNOSTICO HOSPITALARIO")
ventana.geometry("720x600")
ventana.config(bg="white")
ventana.iconphoto(False, tk.PhotoImage(width=1, height=1))

tk.Label(ventana, text="+ SISTEMA DE DIAGNOSTICO HOSPITALARIO", font=("Arial", 16, "bold"), bg="#8b1e2d", fg="white", pady=12).pack(fill="x")
tk.Label(ventana, text="Registro de paciente y signos vitales", font=("Arial", 10), bg="#f2f2f2", fg="#555555", pady=5).pack(fill="x")

datos = tk.Frame(ventana, bg="white", relief="solid", bd=1)
datos.pack(padx=20, pady=15)

tk.Label(datos, text="Nombre:", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=0, column=0, padx=8, pady=6)
nombre = tk.Entry(datos, font=("Arial", 10), width=18)
nombre.grid(row=0, column=1, padx=8, pady=6)

tk.Label(datos, text="Edad:", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=0, column=2, padx=8, pady=6)
edad = tk.Entry(datos, font=("Arial", 10), width=18)
edad.grid(row=0, column=3, padx=8, pady=6)

tk.Label(datos, text="Oxigenacion (%):", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=1, column=0, padx=8, pady=6)
oxigenacion = tk.Entry(datos, font=("Arial", 10), width=18)
oxigenacion.grid(row=1, column=1, padx=8, pady=6)

tk.Label(datos, text="Frecuencia cardiaca (lpm):", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=1, column=2, padx=8, pady=6)
frecuencia = tk.Entry(datos, font=("Arial", 10), width=18)
frecuencia.grid(row=1, column=3, padx=8, pady=6)

tk.Label(datos, text="Presion arterial (mmHg):", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=2, column=0, padx=8, pady=6)
presion = tk.Entry(datos, font=("Arial", 10), width=18)
presion.grid(row=2, column=1, padx=8, pady=6)

tk.Label(datos, text="Peso (kg):", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=2, column=2, padx=8, pady=6)
peso = tk.Entry(datos, font=("Arial", 10), width=18)
peso.grid(row=2, column=3, padx=8, pady=6)

tk.Label(datos, text="Talla (cm):", bg="white", font=("Arial", 10), anchor="e", width=22).grid(row=3, column=0, padx=8, pady=6)
talla = tk.Entry(datos, font=("Arial", 10), width=18)
talla.grid(row=3, column=1, padx=8, pady=6)

def diagnosticar():
    P = int(oxigenacion.get()) < 90
    Q = int(frecuencia.get()) < 60 or int(frecuencia.get()) > 100
    R = int(presion.get()) > 140

    imc = float(peso.get()) / (float(talla.get()) / 100) ** 2
    S = imc >= 25

    texto = "Diagnostico:\n"

    if P:
        texto += "Sintoma: oxigenacion baja\nRecomendacion: administrar oxigeno y mantener al paciente en reposo\n"
    if Q:
        texto += "Sintoma: frecuencia cardiaca fuera de rango\nRecomendacion: descansar\n"
    if R:
        texto += "Sintoma: presion arterial alta\nRecomendacion: reducir sal\n"
    if S:
        texto += "Sintoma: sobrepeso (IMC alto)\nRecomendacion: mejorar la dieta y hacer ejercicio\n"

    cantidad = P + Q + R + S

    if cantidad == 0:
        texto += "\nNivel de riesgo: bajo\n"
        texto += "Estado: paciente estable, continuar con revisiones de rutina\n"
    elif cantidad <= 2:
        texto += "\nNivel de riesgo: medio\n"
        texto += "ADVERTENCIA: el paciente debe acudir a consulta medica\n"
    else:
        texto += "\nNivel de riesgo: alto\n"
        texto += "PELIGRO: el paciente debe ser atendido en urgencias\n"

    numero_cita = random.randint(1, 20)

    texto += "\nCita generada:\n"
    texto += "Numero de cita: " + str(numero_cita) + "\n"
    texto += "Fecha: " + str(numero_cita) + "/10/2026\n"
    texto += "Hora: 10:00\n"
    texto += "\nResumen del paciente:\n"
    texto += "Nombre: " + nombre.get() + "\n"
    texto += "Edad: " + edad.get() + "\n"
    texto += "Sintomas detectados: " + str(cantidad)

    resultado.delete("1.0", "end")
    resultado.insert("end", texto)

boton = tk.Button(ventana, text="Diagnosticar", command=diagnosticar, bg="#8b1e2d", fg="white", font=("Arial", 11, "bold"), padx=30, pady=6)
boton.pack(pady=(0, 15))

tk.Label(ventana, text="Hoja de diagnostico", font=("Arial", 12, "bold"), bg="white", fg="#8b1e2d", anchor="w").pack(fill="x", padx=20)

hoja = tk.Frame(ventana, bg="white")
hoja.pack(fill="both", expand=True, padx=20, pady=(5, 20))

barra = tk.Scrollbar(hoja)
barra.pack(side="right", fill="y")

resultado = tk.Text(hoja, font=("Arial", 10), relief="solid", bd=1, padx=10, pady=10, yscrollcommand=barra.set)
resultado.pack(fill="both", expand=True)

barra.config(command=resultado.yview)

ventana.mainloop()