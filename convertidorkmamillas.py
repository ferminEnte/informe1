x=input("si desea convertir millas a km escriba el numero 1, de lo contrario escriba el numero 0: ")
if (x=="1"):
    m=float(input("ingrese el numero de millas: "))
    print("el numero de millas en km es: ",m*1.01)
else:
    k=float(input("ingrese el numero de km: "))
    print("el numero de km en millas es: ",k/1.01)
    