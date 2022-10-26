#-------------------------------------------------------------------------------------
# 00 - Import dos arquivos e libs correlacionados a estes comandos
from encripta import encriptar_cesar
from decripta import decriptar_cesar
import os, time
#-------------------------------------------------------------------------------------  
# 01 - Vou capturar a MENSAGEM do usuario
mensagem = ""
decisao = ""
comando = 1

time.sleep(1)
os.system('cls')

while (comando == 1): 
    mensagem = input("Digite sua mensagem: \n -> ")

    decisao = input("Está certo da mensagem? \n 'y' = yes or 'n' = no \n -> ")

    if (decisao == 'y' or decisao =='Y'): 
        comando = 0
        time.sleep(1)
        os.system('cls')

    elif(decisao == 'n' or decisao =='N'):
        print("Entendido, vamos recomeçar o processo para que possas registrar a mensagem correta.\n")

    else:
        print("O valor inserido não está nas opções, por favor recomece o processo com calma.\n")

#-------------------------------------------------------------------------------------  
# 02 - Vou capturar o CÓDIGO DE CRIPTOGRAFIA do usuario
codigoSeg = 0
decisao_codigo = ""
comando_codigo = 1


while (comando_codigo == 1): 

    while codigoSeg <= 0 or codigoSeg > 99999999999999:
        print("Valores aceitáveis são: >ZERO e <99999999999999.")
        codigoSeg = int(input("Digite o NUMERO de código para criptografar: "))

    if codigoSeg <= 0 or codigoSeg > 99999999999999:
        print("Valor inválido, por favor insira novamente o NUMERO válido.")
        print("Valores aceitáveis são: >ZERO e <99999999999999.")
        time.sleep(1)
        os.system('cls')

    decisao_codigo = input("Está certo do código? \n 'y' = yes or 'n' = no \n -> ")

    if (decisao_codigo == 'y' or decisao_codigo =='Y'): 
        comando_codigo = 0
        time.sleep(1)
        os.system('cls')

    elif(decisao == 'n' or decisao =='N'):
        print("Entendido, vamos recomeçar o processo para que possas registrar o código correto.\n")

    else:
        print("O valor inserido não está nas opções, por favor recomece o processo com calma.\n")

#-------------------------------------------------------------------------------------  
# 03 - Chamada das funções de manipulação da informação coletada

#Agora que temos a mensagem 'mensagem' e o código 'codigoSeg', vamos manipular os dados

#Chamados e teste das funcoes
mensagemEncriptada = encriptar_cesar(mensagem, codigoSeg)
mensagemDecriptada = decriptar_cesar(mensagemEncriptada, codigoSeg)

#-------------------------------------------------------------------------------------  
# 04 - Impressões das informações
i = 0
while i <=4:
    print("Encriptando mensagem!")
    i += 1
    time.sleep(0.7)
    os.system('cls')

print ("\nMensagem ENCRIPTADA = ", mensagemEncriptada)
time.sleep(1)
print ("\nMensagem DECRIPTADA = ", mensagemDecriptada, "\n")
