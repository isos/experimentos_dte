# experimentos_dte
Este repositorio es para unir diferentes experimentos con dte


dteweb:
=======

Servidor autónomo realizado en Werkzeug.
========================================

- Renderiza un archivo invoice, por medio de jinja2.
- El objetivo es, en un entorno aislado de Odoo, generar un 
  documento de salida con el formato que requiere el SII.
- El archivo invoice.html generado sirve para portar el mismo a
  qweb.
- Al inicio de esta prueba, el archivo test.png es mostrado en forma
  estática. Por ahora ese archivo es generado por otro proceso, el cual 
  se incorporará en próximo commit.
- el código de dteweb, permite tener el servidor levantado y hacer cambios
  en el mismo código, o en los archivos, sin bajar y volver a levantar.
- El archivo parsedxml.py contiene un diccionario con los datos que 
  se envían al renderizador. Coinciden con los datos que deberían
  provenir desde Odoo para realizar la impresión.


Qué requiere para correr:
- Werkzeug
- Jinja2

Como se usa:

    python dteweb.py

    Visitar localhost:5000 para ver el resultado.

El objetivo de este desarrollo es hacer una prueba de concepto de:
- Renderizar los valores que vienen desde el diccionario
- Disponer de un documento de ejemplo con el formato adecuado a las resoluciones, que pueda ser portado después a qweb.


parse_timbre
============

Para qué sirve
- Genera el timbre electrónico a partir de un timbre patron, al cual se le reemplazan valores.

Que requiere para correr (sudo pip install ...)
- xmltodict
- dicttoxml
- elaphe
- cchardet

Como se usa:

	python parsetimbre.py


firma_semilla
=============

Prueba de funcionamiento de firma de semilla utilizando maullin (servidor de homologación del SII).
Requiere tener firma digital (key y pub) en formato pem (cada uno debe usar la suya, ya que no se pueden
utilizar para pruebas/homologación claves autofirmadas ni tampoco hay una previsión de proveer estas
para pruebas por parte del SII).
Codigo tomado del sitio edreams.cl y adaptado.

Requerimientos:

Instalación de las siguientes dependencias:

- sudo apt-get install libxml2-dev
- sudo apt-get install libxslt1-dev
- sudo apt-get install libxmlsec1-dev
- sudo apt-get install python2.7-dev
- sudo pip install --upgrade lxml (>=3)
- sudo pip install dm.xmlsec.binding
- sudo pip install soappy


Como se usa:

	python semilla1.py

Anotaciones Varias DTE CL
=========================

revisar el siguiente archivo:

anotaciones_varias_dte_cl.txt