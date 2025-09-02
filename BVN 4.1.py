def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':  
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z': 
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:  
            result += ch
    return result

def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)


k = 10
plaintext = "Tram"
ciphertext = caesar_encrypt(plaintext, k)

print("k =", k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypt:", caesar_decrypt(ciphertext, k))

