# -*- coding: iso-8859-1 -*-
import M2Crypto, base64, hashlib

class i(object):

    def digest(self, data):
        sha1 = hashlib.sha1()
        sha1.update(data)
        return sha1.digest()
    
    
    def signmessage(self,dd,privkey,pubk):
        ddd = self.digest(dd)
        CafPK = M2Crypto.RSA.load_key_string(privkey)
        #CafPK = M2Crypto.RSA.load_key('cafkey.pem')
    
        firma = CafPK.sign(ddd)
        FRMT = base64.b64encode(firma)
    
        print FRMT
    
        bio = M2Crypto.BIO.MemoryBuffer(pubk)
        rsa = M2Crypto.RSA.load_pub_key_bio(bio)
        pubkey = M2Crypto.EVP.PKey()
        pubkey.assign_rsa(rsa)
    
        # if you need a different digest than the default 'sha1':
        pubkey.reset_context(md='sha1')
        pubkey.verify_init()
        pubkey.verify_update(dd)
        if pubkey.verify_final(firma) == 1:
            return FRMT