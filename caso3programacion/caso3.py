# obtenga el  numero de la suerte con su fecha de nacimiento

dia=int(input("digite su dia de nacimiento: "))
mes=int(input("digite su mes de nacimiento: " ))
año=int(input("digite su año de nacimiento: ")) 
# sumamos los datos solicitados 

resultado= (dia) + (mes) + (año) 
print(resultado)
suma=0
while resultado !=0:
    suma=suma + (resultado % 10)
    resultado=resultado // 10 
print("su numero de la suerte es ",suma) 
