''' Extremely Simple but Effective Crypto'''
class ESEC():
    def __init__(self):
        print("instantiated")
    def encodefortext(self, value):
        import base64
        return base64.b32encode(value)

    def decodefromtext(self, value):
        import base64
        return base64.b32decode(value)
        # initialization (constructor) code goes here
    def generatehash(self, salt, value):
            import hashlib
            h = hashlib.sha256(salt.encode('utf-8')).hexdigest()
            while len(h) < len(value) or len(h) < 2000:
                h = h + hashlib.sha256(h.encode('utf-8')).hexdigest()
            #print(h)
            return h
    def encrypt(self,value, salt):
        h = self.generatehash(salt,value)
        s = bytearray()
        i=0
        for x in value:
            i = i + 1
            y = ord(x) + ord(h[i])
            if y > 256:
                y = y- 256
            #print(y)
            s.append(y)
        return self.encodefortext(s)
    def decrypt(self,value, salt):
        s = self.decodefromtext(value)
        h = bytearray(self.generatehash(salt,value).encode('utf-8'))
        r = ""
        i=0
        for x in s:
            i = i + 1
            y = x - h[i]
            if y < 0:
                y = y+ 256
            #print(y)
            r+= chr(y)
        return r


'''#unit test type thing
e = ESEC()
result = e.encrypt("/usr/bin/python2.7 /home/twist/PycharmProjects/PythonCrypto/ESECrypto.py", "tester")
print(result)
desult = e.decrypt(result, "tester")
print(e.decrypt("kdfUp5KXnM9fpa2pzZ/Ral5oWGPKqKGbYKmqzKzaZIism5/Gpc+0o9OeysinqGaEqdqaqM+mpN6npaeRc6Oy0tjUj6Pe", "tester"))
print("\r\n"+desult)
'''
