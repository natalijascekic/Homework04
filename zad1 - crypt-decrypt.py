#kriptovanje, dekriptovanje

def encrypt(word):
    enc_word = ""
    for character in word:
        enc_char = chr(ord(character) * 2)
        enc_word += enc_char

    return enc_word


def decrypt(enc_word):
    word = ""

    for enc_char in enc_word:
        character = chr(ord(enc_char) // 2)
        word += character

    return word


if __name__ == "__main__":
    kriptovana_rijec = encrypt("Natalija Scekic 16/068")
    print(kriptovana_rijec)

    rijec = decrypt(kriptovana_rijec)
    print(rijec)