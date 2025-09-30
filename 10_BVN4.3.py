
p = 17
q = 23
e = 5
n = p * q  


plaintext = "Nguyễn Ngọc Trâm"

def rsa_encrypt_bytes(text, e, n):
    byte_data = text.encode('utf-8')  
    cipher = [pow(byte, e, n) for byte in byte_data]
    return cipher


cipher_text = rsa_encrypt_bytes(plaintext, e, n)

print("Bản mã RSA:", cipher_text)
