def suma(Num1,Num2):
    Resultado=Num1+Num2
    return print(Resultado)

def resta (Num1,Num2):
    Resultado=(Num1-Num2)
    return print(Resultado)

def multiplicacion(Num1,Num2):
    Resultado=str(Num1*Num2)
    return print(Resultado)
def division(Num1,Num2):
    try:
        Resultado=(Num1/Num2)
        return print(Resultado)
    except ZeroDivisionError:
        return print ("Error")

    

Nombre=input("Ingrese su nombre: ")

print("Hola ",Nombre," este programa realiza todas las funciona basicas ")
print("suma = + \nresta= - \nmultiplicacion = * \ndivicion= / ")

while True:
    num1=int (input("Ingrese la primera cifra: "))
    operador=input ("Ingrese el operador: ")
    num2=int(input("ingrese la segunda cifra: "))


    if operador == "+":
        suma (num1,num2)
    elif operador == "-":
        resta(num1,num2)
    elif operador == "*":
        multiplicacion(num1,num2)
    elif operador == "/":
        division(num1,num2)
    else :
        print("Error ") 


    




