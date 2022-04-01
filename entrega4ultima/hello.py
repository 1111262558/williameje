contar=0
texto=input("digite:  ")
alfabeto="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuWwXxYyZz"
for i in texto:
    if i in alfabeto:
        contar+=1
        
    else:
        print("se encontraron caracteres no alfabeticos")
        break
if contar==len(texto):
    print("se encontraron que todos los caracteres son alfabeticos")