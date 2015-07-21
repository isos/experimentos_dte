# -*- coding: utf-8 -*-
# hardcoded head, partner and lines for an invoice
# in the near future, replace this code with a method of:
# if invoice must be red from odoo, via ws, a ws environment
# if a module inside odoo, read as variables
# if an xml is imported from a partner, or from sii, a parsed
#       reader (xmltodict)
# add the following, some place
# l10n_cl_xml2odoo
# l10n_cl_odoo2xml
# l10n_cl_xml2web
#           or l10n_cl_xml2qweb
# web2xml (?no)


head = {
	'company_name':'SOCIEDAD DE SERVICIOS HECTOR DANIEL BLANCO EIRL',
	'company_slogan':u'Blanco Martín y Asociados :: Los Expertos en ERP',
	'company_logo':'/static/bmyacl.png',
	'company_vat':'76.201.224-3',
	'sii_document_class_id':['1','FACTURA'],
	'sii_document_number':'737373',
	'company_sii_location':'SANTIAGO CENTRO',
	'prim_company_address':'Ahumada 254 Of 1301',
	'prim_company_comuna':'Santiago Centro',
	'prim_company_city':'Santiago',
	'prim_company_country':'Chile',
	'sec_company_address':'Apoquindo 6410 Of 212',
	'sec_company_comuna':'Las Condes',
	'sec_company_city':'Santiago',
	'sec_company_country':'Chile',
	'prim_company_phone':'+56228400990',
	'prim_company_fax':'+56229790208',
	'date_invoice':'28-02-2015',
	'date_due':'10-03-2015',
	'payment':'15 d ff',
	'res_partner_contact_name':'Jose Contreras',
	'res_partner_salesman_name':'Rene Rojas',
	'amount_untaxed':134000,
	'amount_tax':10000,
	'amount_total':144000,
	'company_sii_resolution_number':'54',
	'company_sii_resolution_year':'2013'
}
partner = {
    'name':'ACEPTA S.A.',
    'vat':'CL76201517K',
    'activity_name':'SERVICIOS DE CERTIFICACION DE FIRMAS',
    'street':'La Calle 1234',
    'state_id':[3737,'Santiago Centro/Santiago/Sgo'],
    'city':'SANTIAGO'
}

lines = [
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[CERTWEBV23.0] RENOVACION CERTIFICADO WEB',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':50400,
        'price_subtotal':50400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
    {
        'name':'[FRMDIGV3.0] FIRMA DIGITAL CLASE 3',
        'quantity':'1',
        'discount_perc':0,
        'discount_amount':0,
        'price_unit':23400,
        'price_subtotal':23400,
        'vat_percentage':19,
    },
]
