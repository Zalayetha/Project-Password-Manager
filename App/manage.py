import hashlib
from Crypto.Cipher import AES
import base64
def encrypt(hash_string):
    global b64_encrypt
    def pad_msg(msg):
        while len(msg) % 16 != 0:
            msg += " "
        return msg

    password = "Thisisthekey".encode()
    key = hashlib.md5(password).digest()
    mode = AES.MODE_CBC
    IV = 16 * b'\x00'
    cipher = AES.new(key, mode, IV=IV)

    new_message = pad_msg(hash_string)
    encrypted = cipher.encrypt(new_message.encode())
    # print(type(encrypted))
    b64_encrypt = base64.b64encode(encrypted)
    # print(b64_encrypt)

def decrypt(hash_string):
    password = "Thisisthekey".encode()
    key = hashlib.md5(password).digest()
    mode = AES.MODE_CBC
    IV = 16 * b'\x00'
    cipher = AES.new(key, mode, IV=IV)
    b64_decrypt = base64.b64decode(hash_string)
    # print(b64_decrypt)
    decrypted = cipher.decrypt(b64_decrypt)
    return decrypted.rstrip().decode()