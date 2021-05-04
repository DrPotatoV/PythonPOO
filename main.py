nip = 1234
opc = 1
cant = 0
saldo =print("Introduzca una cantidad")
usuario = Objeto() 
usuario.saldo = saldo
print("Si desea consultar su saldo, presione 1")
print("Si desea realizar un retiro, presione 2")
print("Si desea hacer un deposito, presione 3")
print("Para salir, presione 4")

if opc == 1:
    print("Ha seleccionado consultar su saldo")
    print("Su saldo es de :" + usuario.saldo + " pesos")
if opc == 2:
    print("Ha seleccionado retirar")
    cant = print("Que cantidad desea retirar:")
    if cant <= usuario.saldo:
        usuario.saldo = usuario.saldo - cant
    else:
        print("El monto excede su saldo")

if opc == 3:
    print("Ha seleccionado depositar")
    cant = double(print("Que cantidad desea depositar:"))
    print("Deposito exitoso")
if opc == 4:
    print("Gracias por usar un cajero nuestro, nos vemos pronto")


'''print("Ejemplo de POO")
class Coche():
    ruedas=4
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")
miVehiculo=Coche()
print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")
miVehiculo.desplazamiento()
print("---------------Segundo objeto---------------")
miVehiculo2=Moto()
print("Mi moto tiene ", miVehiculo2.ruedas, " ruedas")
miVehiculo2.desplazamiento()'''