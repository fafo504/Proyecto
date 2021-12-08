import os

class bancopreguntas:

    def __init__(self):
        self.conteo = 0

    def obtener_dic(self, ruta):
        ruta = os.path.realpath(ruta)
        return os.path.dirname(ruta)

    def getConteo(self):
        return self.conteo

    def leerPreguntas(self, numeroPregunta):
        x = self.obtener_dic(__file__)
        rutaarchivo = os.path.join(x, "Banco de preguntas.txt")
        a = open(rutaarchivo, "r", encoding='UTF8')
        b = a.readlines()
        print(b[numeroPregunta])
        a.close()

    def verificarEntero(self, x):
        while True:
            try:
                x = int(x)
                return x
            except ValueError:
                print("Ingrese un numero")
                x = input()

    def contar(self):
        print("A continuacion se le presentara una serie de preguntas")
        print("Responda con el numero del inciso al cual usted se siente identificado")
        for i in range(18):
            print("pregunta #" + str(i+1))
            self.leerPreguntas(i)
            print("1.Nunca ", "2.En alguna ocasion ", "3.A menudo ", "4.Casi tods los dias")
            verificador = False
            x = input()
            while(verificador == False):
                x = self.verificarEntero(x)
                if(x>4):
                    print("Introduzca un valor aceptado")
                    x = input()
                elif(x>0 and x<=4):
                    self.conteo = self.conteo + (x-1)
                    verificador = True

