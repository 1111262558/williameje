#clase 
class Aprendiz:
    identificacion=1111262558
    nombre="william"
    edad=18
    correo="whgsfdyj@gmail"
    telefono=3165438790
#metodos
    def setIdentificacion(self,identificacion):
        self.identificacion=identificacion
    def getIdentificacion(self):
        return self.identificacion
    
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
    def setEdad(self,edad):
        self.edad=edad
    def getEdad(self):
        return self.edad
    def setCorreo(self,correo):
        self.correo=correo
    def getCorreo(self):
        return self.correo
    def setTelefono(self,telefono):
        self.telefono=telefono
    def getTelefono(self):
        return self.telefono
    # instanciar primer objeto
print("los valores son")
aprendiz1=Aprendiz()
print(aprendiz1.identificacion,aprendiz1.nombre,aprendiz1.edad,aprendiz1.correo,aprendiz1.telefono)
#creando otro objeto
aprendiz2=Aprendiz()
print("informacion APRENDIZ2")
aprendiz2.setIdentificacion(1234876542)
aprendiz2.setNombre("pepito")
aprendiz2.setEdad(13),
aprendiz2.setCorreo("pepito@gmail")
aprendiz2.setTelefono(3219024449)
print("la informacion del aprendiz2 es: {")
