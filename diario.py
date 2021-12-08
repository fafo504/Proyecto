import os
from datetime import datetime


class diario:
    def __init__(self):
        self.p = ""

    def obtenerfecha(self):
        return datetime.today().strftime("%Y-%m-%d")

    def comentarios(self):
        com = open('comentarios.txt', 'r', encoding='UTF8')
        b = com.read()
        print(b)
        com.close()

    def escribircomentario(self):
        com = open('comentarios.txt', 'a', encoding='UTF8')
        com.write(self.obtenerfecha() + "\n")
        com.write(input("Comentarios: ") + '\n')

