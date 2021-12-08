from Usuario import usuario
from AnalisisResultados import analisisresultados
from Perfil import perfil
from bancopreguntas import bancopreguntas
from diario import diario

def verificarEntero(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            print("Ingrese un numero")
            x = input()

def mensajeInicio():
    print("Hola mucho gusto")
    print("Te gustaria: ")
    print("1. Iniciar sesion  2. Crear usuario nuevo  3. Salir")

def menuPrincipal():
    print("Bienvenido que deseas hacer?")
    print("1.Medir mi esteres   2.Ver mi perfil")
    print("3.Escribir en mi diario  4.Ver mi diario")
    print("5.Salir")

def crearUsuario(usuario1):
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contrasena = input("Contrasena: ")
    edad = input("Edad: ")
    sexo = input("Sexo: ")
    usuario1.crearUsuario(nombre, correo, contrasena, edad, sexo)


def main():
    verificador = None
    usuario1 = usuario()
    perfil1 = perfil()
    analisisresultados1 = analisisresultados()
    bancopreguntas1 = bancopreguntas()
    diario1 = diario()

    if usuario1.verificarExistenciaDeUsuario() == 0:
        print("Mucho gusto, parece que es la primera vez que ingresas al programa.")
        print("Creemos un usuario para tu persona.")
        crearUsuario(usuario1)
    else:
        while True:
            mensajeInicio()
            x = input("Ingresa el numero de tu eleccion: ")
            x = verificarEntero(x)
            if x == 1:
                while True:
                    usuario1.usuarioExistente(input("Ingrese su correo: "), input("Ingrese su contrasena: "))
                    if usuario1.getNombre() == "":
                        while True:
                            print("Desea: ")
                            print("1. Intentar de nuevo   2. Crear usuario   3. Salir")
                            x = input("Ingrese su respuesta: ")
                            x = verificarEntero(x)
                            verificador = x
                            if x > 3 or x < 1:
                                print("Por favor digite un numero de los dados")
                                continue
                            else:
                                break
                        if verificador == 1:
                            continue
                        elif verificador == 2:
                            crearUsuario(usuario1)
                            break
                        elif verificador == 3:
                            exit()
            elif x == 2:
                crearUsuario(usuario1)
                break
            elif x == 3:
                exit()
            elif x > 3 or x < 1:
                print("Por favor digite un numero de los mostrados con la opcion.")
                continue

    perfil1.setEdad(usuario1.getEdad())
    perfil1.setSexo(usuario1.getSexo())
    perfil1.setCorreo(usuario1.getcorreo())
    perfil1.setNombre(usuario1.getNombre())

    while True:
        menuPrincipal()
        x = input("Ingrese su el numero de la opcion: ")
        x = verificarEntero(x)
        if x == 1:
            bancopreguntas1.contar()
            a = bancopreguntas1.getConteo()
            analisisresultados1.analisisConteo(a)
            analisisresultados1.seleccionActividades(a)
            perfil1.setNivel(analisisresultados1.getNivel())

        elif x == 2:
            perfil1.__str__()

        elif x == 3:
            diario1.escribircomentario()

        elif x == 4:
            diario1.comentarios()

        elif x == 5:
            exit()

        elif x < 1 or x > 5:
            print("Porfavor elija un numero valido")


if __name__ == "__main__":
    main()
