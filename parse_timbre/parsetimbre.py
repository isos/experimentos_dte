# -*- coding: iso-8859-1 -*-
# codigo para construir xml del timbre
# primero sigo el experimento de leer un xml que tengo en un archivo aparte

import datetime
import xmltodict
import dicttoxml
from elaphe import barcode


from signsharsa import i
i = i()

# esta biblioteca sirve para detectar encoding y cambiarla
# util para codificar en ISO-8859-1
import cchardet
def convert_encoding(data, new_coding = 'UTF-8'):
	encoding = cchardet.detect(data)['encoding']

	if new_coding.upper() != encoding.upper():
		data = data.decode(encoding, data).encode(new_coding)
	return data


def format_vat(value):
    return value[2:10] + '-'+ value[10:]
	
def sii_cod(value):	
	for tip in tiposdoc:
	    if tip['siiname'] == value:
	    	return tip['siicod']

def get_folio(value):
	return 991

# timbre patrón. Permite parsear y formar la tupla patrón corespondiente al documento
timbre  = """<TED version="1.0"><DD><RE>99999999-9</RE><TD>11</TD><F>1</F><FE>2000-01-01</FE><RR>99999999-9</RR><RSR>XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</RSR><MNT>10000</MNT><IT1>IIIIIII</IT1><CAF version="1.0"><DA><RE>99999999-9</RE><RS>YYYYYYYYYYYYYYY</RS><TD>10</TD><RNG><D>1</D><H>1000</H></RNG><FA>2000-01-01</FA><RSAPK><M>DJKFFDJKJKDJFKDJFKDJFKDJKDnbUNTAi2IaDdtAndm2p5udoqFiw==</M><E>Aw==</E></RSAPK><IDK>300</IDK></DA><FRMA algoritmo="SHA1withRSA">J1u5/1VbPF6ASXkKoMOF0Bb9EYGVzQ1AMawDNOy0xSuAMpkyQe3yoGFthdKVK4JaypQ/F8afeqWjiRVMvV4+s4Q==</FRMA></CAF><TSTED>2014-04-24T12:02:20</TSTED></DD><FRMT algoritmo="SHA1withRSA">jiuOQHXXcuwdpj8c510EZrCCw+pfTVGTT7obWm/fHlAa7j08Xff95Yb2zg31sJt6lMjSKdOK+PQp25clZuECig==</FRMT></TED>"""

def pdf417bc(ted):
    bc = barcode(
        'pdf417',
        ted,
        options = dict(
            compact = False,
            eclevel = 5, 
            columns = 13, 
            rowmult = 2, 
            rows = 3
        ),
        margin=20,
        scale=1
    )

    bc.show()
    bc.save('test.png')
    return bc
    

# codigo de autorizacion de folios entregado por SII (para tipo de documento 34)
# despues va a haber que tenerlos metido en un diccionario o tupla, o tabla
# para seleccionar desde ahi el caf de acuerdo al documento.
# tendrá también una asociación one2one por ejemplo, a una secuencia de Odoo
caffile = """
<?xml version="1.0"?>
<AUTORIZACION>
	<CAF version="1.0">
		<DA>
			<RE>76201224-3</RE>
			<RS>SOCIEDAD DE SERVICIOS HECTOR DANIEL BLAN</RS>
			<TD>34</TD>
			<RNG><D>1</D><H>20</H></RNG>
			<FA>2014-01-20</FA>
			<RSAPK><M>yDShk1KFeS0P7M12l6mpYMRy2LalYnMR+VEdnvGjy19xFOeOEgTwNXZaajAtaJfwFrkPoOV9sYacgnsmiuqosQ==</M><E>Aw==</E></RSAPK>
			<IDK>100</IDK>
		</DA>
		<FRMA algoritmo="SHA1withRSA">
			s4ivozzep5Mc+aSyVjJZ6smouuak2WDZc6uXFTs4OHf2cx3y+nwzjBp6x4Pj3oHrRY5xC7O9iZYGtNUTvslseg==
		</FRMA>
	</CAF>
	<RSASK>-----BEGIN RSA PRIVATE KEY-----
	MIIBOgIBAAJBAMg0oZNShXktD+zNdpepqWDEcti2pWJzEflRHZ7xo8tfcRTnjhIE
	8DV2WmowLWiX8Ba5D6DlfbGGnIJ7JorqqLECAQMCQQCFeGu3jFj7c1/zM6RlG8ZA
	gvc7JG5Bogv7i2kUoRfc6R0kF+os36AuBlA1oZErKtv2ymXxojnvppXq39tWyHmj
	AiEA7j07wcaUNZrEwJy+YaXnaypCeBf5EfHsq2DTWi+SgcMCIQDXIYftCCFKVagh
	fP9yAfA6+kb+nnkU2CAQQVgDWStwewIhAJ7TfSvZuCO8gysTKZZumkdxgaVlULah
	SHJAjObKYavXAiEAj2uv81rA3DkawP3/oVagJ1GEqb77YzrACtY6rOYc9acCIFhI
	akF8695xmqziO+I25nLcn0lf2mRdCe9IvdNxvaH+
	-----END RSA PRIVATE KEY-----
	</RSASK>

	<RSAPUBK>-----BEGIN PUBLIC KEY-----
	MFowDQYJKoZIhvcNAQEBBQADSQAwRgJBAMg0oZNShXktD+zNdpepqWDEcti2pWJz
	EflRHZ7xo8tfcRTnjhIE8DV2WmowLWiX8Ba5D6DlfbGGnIJ7JorqqLECAQM=
	-----END PUBLIC KEY-----
	</RSAPUBK>
</AUTORIZACION>
""".replace('<?xml version="1.0"?>','',1)

# hardcodeo de datos a usar en el ensamblado del timbre.
# luego serán entregados por objetos de Odoo
rutcompany = 'CL762012243'
company_name = 'SOCIEDAD DE SERVICIOS HECTOR DANIEL BLANCO EMPRESA INDIVIDUAL DE RESPONSABILIDAD LIMTADA'
res_partner_vat = 'CL762013345'
res_partner_name = 'SOCIEDAD DE SERVICIOS LA MAÑANA DE CORDOBA EMPRESA INDIVIDUAL DE RESPONSABILIDAD LIMTADA'
#res_partner_name = res_partner_name.encode('ISO-8859-1')
account_invoice_amount_total = 234567

account_invoice_line_fields = [
	{'name':'Servicio de Instalación de Cables','nn':99999},
	{'name':'Llevarle el paquete','nn':99999},
]

#raise SystemExit(0)

result = xmltodict.parse(timbre)
#print result['TED']['DD']

resultcaf = xmltodict.parse(caffile)

# esto se debe reemplazar con los valores que están en el módulo l10n_cl_invoice
tiposdoc = [
	{'siicod':'33','siiname':u'Factura Electrónica','siitipo':'dte'},
	{'siicod':'34','siiname':u'Factura no Afecta o Exenta Electrónica','siitipo':'dte'},
	{'siicod':'43','siiname':u'Liquidación Factura Electrónica','siitipo':'dte'},
	{'siicod':'46','siiname':u'Factura de Compra Electrónica','siitipo':'dte'},
	{'siicod':'56','siiname':u'Nota de Débito Electrónica','siitipo':'dte'},
	{'siicod':'61','siiname':u'Nota de Crédito Electrónica','siitipo':'dte'},
	{'siicod':'30','siiname':u'Factura','siitipo':'dte'},
	{'siicod':'32','siiname':u'Factura de Ventas y Servicios no Afectos o Exentos de IVA','siitipo':'dte'},
	{'siicod':'40','siiname':u'Liquidación Factura','siitipo':'dte'},
	{'siicod':'45','siiname':u'Factura de Compra','siitipo':'dte'},
	{'siicod':'55','siiname':u'Nota de Débito','siitipo':'dte'},
	{'siicod':'60','siiname':u'Nota de Crédito','siitipo':'dte'}
]
# rut del emisor. Viene de Odoo con el formato 'CL762012243' y 
# format_vat lo lleva a 76201224-3
result['TED']['DD']['RE'] = format_vat(rutcompany) 
# tipo de DTE. Lo busca de un diccionario json, pero después lo buscará
# del módulo de clases de documentos
result['TED']['DD']['TD'] = sii_cod(u'Factura no Afecta o Exenta Electrónica')
# busca el folio corespondiente a la secuencia asociada al tipo de comprobante.
# actualmente está hardcodeado para las pruebas.
# por lo que no valida si está dentro del rango del CAF asociado
# esto queda para hacer  
result['TED']['DD']['F']  = get_folio(u'Factura no Afecta o Exenta Electrónica')  # Folio
# Fecha de emision en formato AAAA-MM-DD
result['TED']['DD']['FE'] = datetime.date.today()  
# rut del receptor. Vendrá desde res_partner
result['TED']['DD']['RR'] = format_vat(res_partner_vat)  
# nombre o razón social truncado a 40 caracteres
result['TED']['DD']['RSR'] = (res_partner_name[:40]).decode('utf-8')
# monto total de la factura (incluyendo iva si corresponde)
result['TED']['DD']['MNT'] = account_invoice_amount_total
# aca itera las lineas de la factura.
# el break lo hace porque en el timbre coloca solo el primer item de la factura.
for line in account_invoice_line_fields:
	result['TED']['DD']['IT1'] = (line['name']).decode('utf-8')
	break
# esta parte, introduce dentro del documento todo el codigo correspondiente al CAF,
# ahora está tomando uno solo, pero después va a tener que elegir el caf xml de acuerdo
# al tipo de documento que se trate.	
result['TED']['DD']['CAF'] = resultcaf['AUTORIZACION']['CAF']

#print result
dte = result['TED']['DD']
ddxml = '<DD>'+dicttoxml.dicttoxml(dte, root=False, attr_type=False).replace('<key name="@version">1.0</key>','',1).replace('><key name="@version">1.0</key>',' version="1.0">',1).replace('><key name="@algoritmo">SHA1withRSA</key>',' algoritmo="SHA1withRSA">').replace('<key name="#text">','').replace('</key>','')+'</DD>'
# ddxml es el primer componente de la firma 
#print ddxml
# con esta funcion fuerzo la conversion a iso-8859-1
ddxml = convert_encoding(ddxml, 'ISO-8859-1')
#ahora agarro la clave privada y ya tengo los dos elementos que necesito para firmar
keypriv = (resultcaf['AUTORIZACION']['RSASK']).encode('latin-1').replace('\t','')
keypub = (resultcaf['AUTORIZACION']['RSAPUBK']).encode('latin-1').replace('\t','')

frmt = i.signmessage(ddxml,keypriv,keypub)
ted = ('<TED version="1.0">{}<FRMT algoritmo="SHA1withRSA">{}</FRMT></TED>').format(ddxml,frmt)

print ted
print pdf417bc(ted)