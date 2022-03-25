# Master Vector
import subprocess
import sub
import os

dir = os.path.dirname(__file__)
path = dir + "/sub/Suma.py"

def masterprogram():
    print("Elige la operación a realizar")
    print("1. Suma de vectores")
    print("2. Vector por escalar")
    print("3. Resta de vectores")
    print("4. Producto escalar entre dos vectores")
    print("5. Producto escalar de un vector consigo mismo")
    print("6. Modulo de un vector")
    print("7. Distancia entre dos puntos")
    print("8. Angulo entre vectores y perpendicularidad")
    print("9. Producto escalar a partir de angulo y modulo")
    opcion = int(input("Número de operación: "))
    if opcion == 1:
        subprocess.call(dir + "/sub/Suma.py" , shell=True)
    elif opcion == 2:
        subprocess.call(dir + "/sub/Vecescalar.py", shell=True)
    elif opcion == 3:
        subprocess.call(dir + "/sub/Resta.py", shell=True)
    elif opcion == 4:
        subprocess.call(dir + "/sub/Prodvec.py", shell=True)
    elif opcion == 5:
        subprocess.call(dir + "/sub/Prodvecself.py", shell=True)
    elif opcion == 6:
        subprocess.call(dir + "/sub/Modulo.py", shell=True)
    elif opcion == 7:
        subprocess.call(dir + "/sub/Distancia.py", shell=True)
    elif opcion == 8:
        subprocess.call(dir + "/sub/Angulo.py", shell=True)
    elif opcion == 9:
        subprocess.call(dir + "/sub/ProdescAM.py", shell=True)
    else:
        print("opción invalida")

masterprogram()

cont = input("Querés realizar otra operación? Si / No : ")

if cont == "Si" or cont == "si":
    masterprogram()
else:
    quit