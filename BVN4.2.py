import unicodedata

def remove_dau(text):
    nfkd = unicodedata.normalize('NFD', text)
    return ''.join(ch for ch in nfkd if not unicodedata.combining(ch))

def caesar_encrypt(text, k):
    text = remove_dau(text)
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch
    return result


plaintext = "Nguyễn Ngọc Trâm"
k = 10
ciphertext = caesar_encrypt(plaintext, k)

print("Plaintext :", plaintext)
print("Sau khi bỏ dấu:", remove_dau(plaintext))
print("k =", k)
print("Ciphertext:", ciphertext)
