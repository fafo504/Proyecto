import os

class analisisresultados:

    def __init__(self):
        self.Nivel = ""

    def obtener_dic(self, ruta):
        ruta = os.path.realpath(ruta)
        return os.path.dirname(ruta)

    def getNivel(self):
        return self.Nivel

    def setNivel(self, nivel):
        self.Nivel = nivel

    def analisisConteo(self, conteo):
        if(conteo>0 and conteo<=18):
            x = self.obtener_dic(__file__)
            rutaarchivo = os.path.join(x, "Estres Bajo.txt")
            a = open(rutaarchivo, "r", encoding='UTF8')
            b = a.readlines()
            for linea in b:
                print(linea)
            self.setNivel("Bajo")
            a.close()
        elif(conteo>19 and conteo<=36):
            x = self.obtener_dic(__file__)
            rutaarchivo = os.path.join(x, "Estres Moderado.txt")
            a = open(rutaarchivo, "r", encoding='UTF8')
            b = a.readlines()
            for linea in b:
                print(linea)
            self.setNivel("Medio")
            a.close()
        elif(conteo>37 and conteo<=54):
            x = self.obtener_dic(__file__)
            rutaarchivo = os.path.join(x, "Estres Alto.txt")
            a = open(rutaarchivo, "r", encoding='UTF8')
            b = a.readlines()
            for linea in b:
                print(linea)
            self.setNivel("Alto")
            a.close()

    def seleccionActividades(self, nivel):
        if(nivel == "Bajo"):
            x = self.obtener_dic(__file__)
            rutaarchivo = os.path.join(x, "Actividades Nivel Bajo.txt")
            a = open(rutaarchivo, "r", encoding='UTF8')
            b = a.readlines()
            for linea in b:
                print(linea)
                a.close()
        elif(nivel == "Medio"):
            x = self.obtener_dic(__file__)
            rutaarchivo = os.path.join(x, "Actividades Nivel Moderado.txt")
            a = open(rutaarchivo, "r", encoding='UTF8')
            b = a.readlines()
            for linea in b:
                print(linea)
                a.close()
        elif(nivel == "Alto"):
            x = self.obtener_dic(__file__)
            rutaarchivo = os.path.join(x, "Actividades Nivel Alto.txt")
            a = open(rutaarchivo, "r", encoding='UTF8')
            b = a.readlines()
            for linea in b:
                print(linea)
                a.close()
