# In[1]:
 
import dm.xmlsec.binding as xmlsec
xmlsec.initialize()
from os.path import dirname, basename
from lxml.etree import tostring
BASEDIR = dirname(xmlsec.__file__) + "/resources/"
 
 
# In[2]:
 
def getSemilla():
    from SOAPpy import SOAPProxy
    import lxml.etree as ET
    url =  'https://maullin.sii.cl/DTEWS/CrSeed.jws?WSDL'
    ns =  'urn:https://maullin.sii.cl/DTEWS/CrSeed.jws'
    _server = SOAPProxy(url, ns)
    root = ET.fromstring(_server.getSeed())
    semilla = root[0][0].text
    return semilla
 
 
# In[9]:
 
def doTemplateSemilla(semilla2):
    import lxml.etree as ET
    from StringIO import StringIO
    xml_head = u'''    <getToken>
<item>
'''
    xml_body = '<Semilla>' + semilla2 + '</Semilla>'
    xml_footer = '''
</item>
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
<SignedInfo>
<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
<Reference URI="">
<Transforms>
<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
</Transforms>
<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
<DigestValue/>
</Reference>
</SignedInfo>
<SignatureValue/>
<KeyInfo>
<KeyValue>
<RSAKeyValue>
<Modulus/>
<Exponent/>
</RSAKeyValue>
</KeyValue>
<X509Data>
<X509Certificate/>
</X509Data>
</KeyInfo>
</Signature>
</getToken>
'''
    xml =  xml_head + xml_body + xml_footer
    tree = ET.parse(StringIO(xml))
    outFile2 = open('archivo_semilla_template.xml', 'w')
    tree.write(outFile2, xml_declaration=True, encoding='iso-8859-1')
    return
 
 
# In[4]:
 
def firmar_digitalmente_semilla(tmpl_file, key_file, cert_file):
    
    from lxml.etree import parse, tostring
    doc = parse(tmpl_file)
    # find signature node
    node = xmlsec.findNode(doc, xmlsec.dsig("Signature"))
    dsigCtx = xmlsec.DSigCtx()
    # Note: we do not provide read access to `dsigCtx.signKey`.
    #  Therefore, unlike the `xmlsec` example, we must set the key name
    #  before we assign it to `dsigCtx`
    # load tiene el paramtro password vacio, porque el pem que yo genero no esta protegido
    signKey = xmlsec.Key.load(key_file, xmlsec.KeyDataFormatPem, "")
    signKey.loadCert(cert_file, xmlsec.KeyDataFormatPem)
    # Note: the assignment below effectively copies the key
    dsigCtx.signKey = signKey
    dsigCtx.sign(node)
    outFile = open('archivo_semilla_firmada.xml', 'w')
    doc.write(outFile, xml_declaration=True, encoding='iso-8859-1') 
    return tostring(doc)
 
 
 
# In[5]:
 
def getToken(archivo_de_la_semilla):
    from SOAPpy import SOAPProxy
    import lxml.etree as ET
    url =  'https://maullin.sii.cl/DTEWS/GetTokenFromSeed.jws?WSDL'
    ns =  'urn:https://maullin.sii.cl/DTEWS/GetTokenFromSeed.jws'
    _server = SOAPProxy(url, ns)
    tree = ET.parse(archivo_de_la_semilla)
    ss = ET.tostring(tree, pretty_print=True, encoding='iso-8859-1')
    respuesta = ET.fromstring(_server.getToken(ss))
    token = respuesta[0][0].text
    return token
 
 
# In[6]:
 
semilla3 = getSemilla()
print "La Semilla es: " , semilla3
doTemplateSemilla(semilla3)
seed_firmado = firmar_digitalmente_semilla("archivo_semilla_template.xml", "newfile.key.pem", "newfile.crt.pem")
token = getToken("archivo_semilla_firmada.xml")
print "El Token es: " ,token