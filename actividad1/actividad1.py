# 1. Crea una funcion que pida por pantalla un número al usuario y que
# controle mediante excepciones lo siguiente:
# a. Solo se podrá introducir numeros enteros
# b. Si el numero es mayor de 10 lanza una excepción con raise la
# cual hayas creado previamente mediante ‘class
# Miexcepcion(Exception):’

class Miexcepcion(Exception):
    pass

def numero_usuario():
    try:
        numero = int(input("Introduce un número: "))
        if numero > 10:
            raise Miexcepcion("El número no puede ser mayor que 10")
    except ValueError:
        print("Solo se puede introducir número enteros")
    except Miexcepcion as e:
        print("Error:", str(e))    
              
numero_usuario()


# 2. Abre un fichero .txt y controla mediante excepciones las diferentes
# casuisticas para que el programa no termine de forma inesperada.
# Utiliza el finally para cerrar el fichero.

def abrir_archivo(archivo):
    try:
        archivo = open(archivo, 'r')
        contenido = archivo.read()
        print(contenido)
        print("Abrimos archivo")
    except FileNotFoundError:
        print("El archivo no existe")
    except PermissionError:
        print("No se tiene permiso para abrir el archivo")
    except IOError:
        print("Ocurrió un error Input/Output al abrir el archivo")
    finally:
        if archivo:
            archivo.close()
            print("Cerramos archivo")

# Llamada a la función
archivo = "main.txt"
abrir_archivo(archivo)
