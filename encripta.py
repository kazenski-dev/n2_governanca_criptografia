#Codigo para Encriptar
def encriptar_cesar(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    codigoEncriptado = ""

    # Converter todo o texto em minúscula:
    mensagem = mensagem.lower()

    for i in mensagem:

        letraEncriptada = (ord(i) - ord('a') + chave)%26
        codigoEncriptado += alfabeto[letraEncriptada]
    
    return codigoEncriptado