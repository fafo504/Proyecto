import os

class usuario:

    usuarios = 0

    def __init__(self):
        self.nombre = ''
        self.contrasena = ''
        self.correo = ''
        self.edad = ''
        self.sexo = ''
        self.conect = False
        self.inten = 3

        usuario.usuarios += 1

    def getcorreo(self):
        return self.correo

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getSexo(self):
        return self.sexo

    def obtener_dic(self, ruta):
        ruta = os.path.realpath(ruta)
        return os.path.dirname(ruta)

    def verificarExistenciaDeUsuario(self):
        x = self.obtener_dic(__file__)
        rutaarchivo = os.path.join(x, "Usuarios.txt")
        return os.stat(rutaarchivo).st_size

    def crearUsuario(self, nombre, correo, contrasena, edad, sexo):
        x = self.obtener_dic(__file__)
        rutaarchivo = os.path.join(x, "Usuarios.txt")
        a = open(rutaarchivo, "a", encoding='UTF8')
        a.write("\n" + "Usuario: " + str(nombre) + "," + str(correo) + "," + str(contrasena) + "," + str(edad) + "," + str(sexo))
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.edad = edad
        self.sexo = sexo


    def usuarioExistente(self, Correo, Contrasena):
        x = self.obtener_dic(__file__)
        rutaarchivo = os.path.join(x, "Usuarios.txt")
        a = open(rutaarchivo, "r", encoding='UTF8')
        for linea in a:
            linea = linea.strip()
            if linea.startswith("Usuario: "):
                linea = linea.lstrip("Usuario: ")
                linea = linea.split(",")
                if Correo in linea and Contrasena in linea:
                    self.nombre = linea[0]
                    self.correo = linea[1]
                    self.contrasena = linea[2]

        if self.nombre == "":
            print("Datos incorrectos o usuario inexistente.")

    def conectar(self):
        contra = input("ingrese contraseña")
        if contra == self.contrasena:
            print("conectado")
            self.conect = True
        else:
            print("contrasena incorrecta")

    def desconectar(self):
        if self.conect:
            print("seccion finalizada")
            self.conect = False
        else:
            print("Error")

    def __str__(self):
        if self.conect:
            conectado = "conectado"
        else:
            conectado = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conectado}"
