dia=int(input("digite su dia de nacimiento: "))
    mes=int(input("digite su mes de nacimiento: " ))
    año=int(input("digite su año de nacimiento: ")) 
    salir_del_ciclo=int(input("digite su numero si desea contuniar:"))

    resultado= (dia) + (mes) + (año) 

    print(resultado)

suma_resultado=sum([int(i) for i in str(resultado)])
print("su numero de la suerte es ",suma_resultado)     


