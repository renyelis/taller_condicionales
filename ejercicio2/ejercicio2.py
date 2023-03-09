# input
print(".................................")
print(".........INGRESOS................")
print(".................................")


ing= int(input ("ingrese sus ingresos: "))
deuda= int(input("ingrese sus deudas: "))

# output
if ing > 945200:
    if deuda==0:
         rta =("se aprueba el prestamo ")
    else:
        rta =("prestamo no aprobado ")
else:
    rta =("no se aprueba el prestamo ")


# uotput 
print(rta)