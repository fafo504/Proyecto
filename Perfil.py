class perfil:

    def __init__(self):
        self.nivelEstres = 'Test no realizado aun'
        self.edad = ''
        self.sexo = ''
        self.nombre = ''
        self.correo = ''

    def setNivel(self, nivel):
        self.nivelEstres = nivel

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCorreo(self, correo):
        self.correo = correo

    def __str__(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Correo:", self.correo)
        print("El usuario presenta el siguiente nivel de estres:", self.nivelEstres)

