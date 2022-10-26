#Codigo para Decriptar
def decriptar_cesar(criptografado, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    codigoDecriptado = ""

    for i in criptografado:

        numLetraDecriptada = (ord(i) - ord('a') + 26 - chave)%26
        codigoDecriptado += alfabeto[numLetraDecriptada]

    return codigoDecriptado 