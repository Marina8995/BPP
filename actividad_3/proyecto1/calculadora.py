from PyQt5.QtWidgets import *
import sys

def sumar():
    """
    Función para realizar la operación de suma.
    Obtiene los valores de los campos de entrada y muestra el resultado en la etiqueta de resultado.
    """
    num1 = float(entry_num1.text())
    num2 = float(entry_num2.text())
    resultado = num1 + num2
    label_resultado.setText(f"RESULTADO: {resultado}")

def restar():
    """
    Función para realizar la operación de resta.
    Obtiene los valores de los campos de entrada y muestra el resultado en la etiqueta de resultado.
    """
    num1 = float(entry_num1.text())
    num2 = float(entry_num2.text())
    resultado = num1 - num2
    label_resultado.setText(f"RESULTADO: {resultado}")

def multiplicar():
    """
    Función para realizar la operación de multiplicación.
    Obtiene los valores de los campos de entrada y muestra el resultado en la etiqueta de resultado.
    """
    num1 = float(entry_num1.text())
    num2 = float(entry_num2.text())
    resultado = num1 * num2
    label_resultado.setText(f"RESULTADO: {resultado}")

def dividir():
    """
    Función para realizar la operación de división.
    Obtiene los valores de los campos de entrada y muestra el resultado en la etiqueta de resultado.
    Si el segundo número es cero, muestra un mensaje de error.
    """
    num1 = float(entry_num1.text())
    num2 = float(entry_num2.text())
    if num2 == 0:
        label_resultado.setText("No se puede dividir por cero")
    else:
        resultado = num1 / num2
        label_resultado.setText(f"RESULTADO: {resultado}")

# Creamos la aplicación Qt
app = QApplication([])

# Creamos la ventana principal
ventana = QWidget()
ventana.setWindowTitle("CALCULADORA")
ventana.setFixedSize(300, 250)

# Creamos los widgets
layout = QGridLayout(ventana)

label_num1 = QLabel("NUMERO 1:")
layout.addWidget(label_num1, 0, 0, 1, 1)
entry_num1 = QLineEdit()
layout.addWidget(entry_num1, 0, 1, 1, 1)

label_num2 = QLabel("NUMERO 2:")
layout.addWidget(label_num2, 1, 0, 1, 1)
entry_num2 = QLineEdit()
layout.addWidget(entry_num2, 1, 1, 1, 1)

# Creamos los botones de cálculo
boton_sumar = QPushButton("+")
boton_sumar.clicked.connect(sumar)
layout.addWidget(boton_sumar, 2, 0, 1, 1)
"""
Botón para realizar la suma de los dos números ingresados.
Cuando se hace clic en este botón, se llamará a la función 'sumar()'.
"""

boton_restar = QPushButton("-")
boton_restar.clicked.connect(restar)
layout.addWidget(boton_restar, 2, 1, 1, 1)
"""
Botón para realizar la resta de los dos números ingresados.
Cuando se hace clic en este botón, se llamará a la función 'restar()'.
"""

boton_multiplicar = QPushButton("X")
boton_multiplicar.clicked.connect(multiplicar)
layout.addWidget(boton_multiplicar, 3, 0, 1, 1)
"""
Botón para realizar la multiplicación de los dos números ingresados.
Cuando se hace clic en este botón, se llamará a la función 'multiplicar()'.
"""

boton_dividir = QPushButton("/")
boton_dividir.clicked.connect(dividir)
layout.addWidget(boton_dividir, 3, 1, 1, 1)
"""
Botón para realizar la división de los dos números ingresados.
Cuando se hace clic en este botón, se llamará a la función 'dividir()'.
"""

# Creamos la etiqueta de resultado
label_resultado = QLabel("RESULTADO:")
layout.addWidget(label_resultado, 4, 0, 1, 1)

# Mostramos la ventana
ventana.show()

# Ejecutamos la aplicación
app.exec_()
