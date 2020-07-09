# spmail
Spmail es un mail spoofer con la finalidad de explicar el funcionamiento de estos 
Lo fácil que puede ser suplantar mails para que un scam te robe tus datos

## instalación
Para instalarlo primero debes tener python instalado, para termux y distribuciones Linux puedes escribir 
```
pkg install python
```
Para Windows lo puedes descargar en la <a href="https://www.python.org/downloads/"> página oficial de descarga</a>
y ponerlo en el path 


Ahora ocupamos instalar requests para ello ejecutamos en la terminal
```
pip install requests
```

También ocuparemos git para ello ejecutamos 
```
pkg install git
```

Ahora clonamos el repositorio
``` 
git clone https://github.com/xKatooo/spmail.git
```

## USO 
Una vez ya instalado no necesitamos más que abrirlo

Primero abrimos la carpeta en la que está el archivo 
```
cd /spmail
```

Ahora ejecutamos el script 
```
./spmail
```

Llenamos los datos y este enviara el correo falso

Para enviar un correo en HTML pega tu código en el archivo 'html.txt'

NO NOS HACEMOS RESPONSABLES DE EL USO QUE SE LE DE A ESTA HERRAMIENTA, SOLO TIENE LA FINALIDAD DE ESTUDIAR Y COMPRENDER LA FACILIDAD CON LA QUE SE PUEDE ENGAÑAR A UNA PERSONA CON DATOS FALSOS 

# Para contribuidores
Puedes contribuir desde Pull requests en el archivo "mails.txt" en dónde puedes agregar los dominios que hayas probado y no envíen el correo, también puedes contribuir al código python o con otro php más eficiente 

