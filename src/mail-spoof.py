#!/usr/bin/python
# coding=utf-8
import requests
from os import remove
from os import path
import os
import sys
from colorama import init
init(autoreset = True)

import platform
sistema = platform.system()

banner = """\033[35m
   _____ _____  __  __       _ _ 
  / ____|  __ \|  \/  |     (_) |
 | (___ | |__) | \  / | __ _ _| |
  \___ \|  ___/| |\/| |/ _` | | |
  ____) | |    | |  | | (_| | | |
 |_____/|_|    |_|  |_|\__,_|_|_|
                                 
                                 \033[32mCreado por xKatooo

                                 \033[32mGithub.com/xKatooo
"""
print(banner)
print ("""\033[31m
Que deseas hacer?
1) iniciar
2) salir
""")

respuestaaa = input("\033[31m > ")

if respuestaaa == "2":
    print("\033[36mOki, byeee ^-^ ")
    sys.exit()


if __name__ == '__main__':
    if sistema == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    
    os.system(clear)
    print (banner)

    vic = input("Escribe el correo de la Víctima: ")
    de = input("Escribe el correo del Remitente: ")
    rev = de.find('@')
    dom = (de[rev:])
    archivo = "./src/mails.txt"
    f = open (archivo)
    buscar = f.read()
    n = buscar.count(dom)
    f.close
    if n == 1:
        os.system("clear")
        print (banner)
        print ('''

        Este correo no se puede suplantar
        Meow :(

            ''')
    else:
        asu = input("escribe el asunto: ")
        tipo = input("Tu correo estara en html (presiona 'h') o Sera solo texto? (presiona solo 't'): ")
        if tipo == 'h':
            print ("""
            Se Enviara El Contenido De html.txt
            """)
            f = open ('../html.txt','r')
            msg = f.read()
            url = 'https://katomail002.000webhostapp.com/enviado.php'
            args = {
                'to':''+vic+'',
                'subject':''+asu+'',
                'message':''+msg+'',
                'from':''+de+''
            }
            response = requests.post(url, data=args)
            if response.status_code == 200:
                os.system(clear)
                print (banner)
                print(response.text)
                print("""
            Estos son tus Datos:
                """)
                print ("De : " + de)
                print ("Para : " + vic)
                print ("Asunto : " + asu)
                print ("Mensaje : " + msg)
                f.close()
            else:
                os.system(clear)
                print (banner)
                print('Error de pagina, Avisale a Kato Codigo:001')
                
        else:
            msg=input("Escribe el mensaje: ")
            url = 'https://katomail002.000webhostapp.com/enviado.php'
            args = {
                'to':''+vic+'',
                'subject':''+asu+'',
                'message':''+msg+'',
                'from':''+de+''
            }
            response = requests.post(url, data=args)
            if response.status_code == 200:
                os.system(clear)
                print (banner)
                print(response.text)
                print("""
                Estos son tus Datos:
                """)
                print ("De : " + de)
                print ("Para : " + vic)
                print ("Asunto : " + asu)
                print ("Mensaje : " + msg)
                f.close()
            else:
                os.system(clear)
                print (banner)
                print('Error de pagina, Avisale a Kato Codigo : 002')
else:
    print("algo anda mal :(!")


