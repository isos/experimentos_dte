'''
Este codigo solo contiene un XML de ejemplo
'''
xmlpat = '''<DTE version="1.0" >
      <Documento ID="{}">
        <Encabezado>
          <IdDoc>
            <TipoDTE>{}</TipoDTE>
            <Folio>{}</Folio>
            <FchEmis>{}</FchEmis>
          </IdDoc>
          <Emisor>
            <RUTEmisor>{}</RUTEmisor>
            <RznSoc>{}</RznSoc>
            <GiroEmis>{}</GiroEmis>
            <Acteco>{}</Acteco>
            <Sucursal>{}</Sucursal>
            <DirOrigen>{}</DirOrigen>
            <CmnaOrigen>{}</CmnaOrigen>
            <CiudadOrigen>{}</CiudadOrigen>
          </Emisor>
          <Receptor>
            <RUTRecep>{}</RUTRecep>
            <CdgIntRecep>{}</CdgIntRecep>
            <RznSocRecep>{}</RznSocRecep>
            <GiroRecep>{}</GiroRecep>
            <DirRecep>{}</DirRecep>
            <CmnaRecep>{}</CmnaRecep>
            <CiudadRecep>{}</CiudadRecep>
          </Receptor>
          <Totales>
            <MntExe>{}</MntExe>
            <MntTotal>{}</MntTotal>
          </Totales>
        </Encabezado>
<!-- ACA VA LA ITERACION DE LOS ITEMS FACTURADOS DESDE -->
        <Detalle>
          <NroLinDet>{}</NroLinDet>
          <NmbItem>{}</NmbItem>
          <DscItem>{}</DscItem>
          <MontoItem>{}</MontoItem>
        </Detalle>
<!-- ACA VA LA ITERACION DE LOS ITEMS FACTURADOS HASTA -->        
<!-- ACA VA EL TED DESDE -->
        {}
<!-- ACA VA EL TED HASTA -->
        <TmstFirma>{}</TmstFirma>
      </Documento>
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
        <CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
        <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />
        <Reference URI="#F1946282T34">
            <Transforms>
                <Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />
            </Transforms>
            <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />
            <DigestValue>{}</DigestValue>
        </Reference>
    </SignedInfo>
<SignatureValue>{}</SignatureValue>
<KeyInfo>
    <KeyValue>
        <RSAKeyValue>
            <Modulus>{}</Modulus>
            <Exponent>{}</Exponent>
        </RSAKeyValue>
    </KeyValue>
<X509Data>
    <X509Certificate>
    {}
    </X509Certificate>
</X509Data>
</KeyInfo>
</Signature>
</DTE>'''
