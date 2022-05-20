# operador opcional
def listanew():
    lista=[]
    for i in range(10):
        valor=input(":: Ingrese Un Elemento:  ::")
        lista.append(valor)  
    return lista

def devolverlista(lista):
        print(",".join(map(str,lista)))       
def ordenarlista(lista):
    print(sorted(lista))
   
def revertlista(lista):
    lista.sort(reverse=True)
    print(lista)

def elemento(lista):
    if valor in lista:
        lista.index(valor)
        print(f':: La Longitud De La Lista es:   :: ',len(lista))
#Programa Principal
lista=listanew()
print("El Contenido De La lista es : ", lista)    
rango=devolverlista(lista)
ordenarlista(lista)
revertlista(lista)
valor=input(":: Ingrese Un Elemento:  ::")
print(lista.index(valor))
elemento(lista)