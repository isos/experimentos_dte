# -*- coding: utf-8 -*-

"""pruebas de codificacion varias.
   estas pruebas tienen por objeto evaluar diferentes
   sistemas de cambio de codificacion desde utf-8
   a otras cosas
"""

unicodestring = u"Añoramos la solución"
print unicodestring
# Convert Unicode to plain Python string: "encode"
utf8string = unicodestring.encode("utf-8")
print utf8string.decode("utf-8").encode("ISO-8859-1")
#asciistring = unicodestring.encode("ascii")
#print asciistring
isostring = unicodestring.encode("ISO-8859-1")
print isostring
utf16string = unicodestring.encode("utf-16")
# Convert plain Python string to Unicode: "decode"
plainstring1 = unicode(utf8string, "utf-8")
#plainstring2 = unicode(asciistring, "ascii")
plainstring3 = unicode(isostring, "ISO-8859-1")
plainstring4 = unicode(utf16string, "utf-16")
#assert plainstring1 == plainstring2 == plainstring3 == plainstring4
