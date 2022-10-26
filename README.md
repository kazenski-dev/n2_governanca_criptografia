# n2_governanca_criptografia
Repositório para alocar os códigos de criptografia desenvolvidos na disciplina de Governança em TI do Cesusc.

- N2 - Eduardo Kazenski e Daniel Beira
- Professor Fabiano
- Governanca em TI - Cesusc

## Explicação da lógica, do código e das escolhas feitas:

- [X] Nós utilizamos a linguagem python pela facilidade e clareza que EU EDUARDO enxergo na mesma. Acho que é limpa e atende questões simples como esta. A linguagem tem manipulações com string  bem completas e sem comandos complexos, quando comparado a Java e afins.

- [X] A construção em si foi feita baseado em entender que dentro de um conjunto de caracteres pré definidos devemos encontrar a letra inserida; pegando a letra na posição conforme o código que recebi do usuário.
 
- [X] Essa lógica fez pensar em 2 cenários:
a - encontrar a localização de cada letra pelo 'FIND' do python que é o oposto do operador []. Em vez de pegar um índice e extrair o caractere correspondente, ela pega um caractere e encontra (finds) em qual índice aquele caractere aparece. 
b - percorrer as letras conforme o índice delas dentro da string alfabeto.

- [X] Temos que frisar que pensamos em manipular o andamento das letras dentro de vetor e afins, contudo buscamos algo matemático para ajudar nisso porque chegando a seleção na letra 'z' não tenho uma lista encadeada pra isso, desta forma vamos calcular os valores numericos das letras pra reiniciar o foco da busca.
O alfabeto neste código tem 26 letras e vamos utilizar o conhecimento de módulo e matemática. Acabamos nos obrigando a usar a ideia de trabalhar com os valores dos códigos Unicode, e para manipular esses valores eu usamos a função 'ord()', contudo transformando em valores simbólicos de 1 a 26.
A lógica é enxergar na string alfabeto 'abcdefghijklmnopqrstuvwxyz' cada letra como um índice de 1 a 26, desta forma conseguimos enxergar que, quando a letra tiver que exceder o meu último valor 'z', ele aplica módulo e o resto significa o valor que reinicia a contagem da letra.

- [X] Tentamos criar regras dentro da lógica para manter o backspace, contudo, não obtivemos sucesso dentro do timebox da atividade. Incluir esse caractere de valor Unicode diferente irira quebrar a lógica. Desta forma, o código somente manipula mensagem sem backspace, e se caso inserido o backspace, ele entende como letra 'n' pois vai aplicar a lógica de movimentação circular na string com o valor de backspace até chegar a um caractere que não tem ligação com o mesmo.

## Construção:
- Neste programa declarei 2 variáveis que receberão dados digitados pelo usuário: mensagem, codigoSeg e confirmações de inserção ('y' para yes/'n' para no).

- [X] Meu código principal ('main.py) está segmentado em:
0. imports necessários
1. captura de mensagem do usuário
2. captura do código do usuário
3. chamada das funções de arquivos dirferentes
4. impressões das informações

- [X] Meu código de encriptar (encripta.py):
1. tem parâmetros de mensagem e chave que veem do código principal 'main.py'
2. listei o alfabeto em string para ser consultada a localização de cada letra necessária
3.  criei uma variável 'codigoEncriptado' para receber a mensagem alterada
4. transformo  em minúsculas todas as letras da string recebida
5. analiso dentro da string varrendo a mensagem recebida e somo a chave recebida a fim de achar o valor encriptado. Vou fazer um append nessa variável encriptada (caractere por caractere), adiconando: o numero do caractere atual menos o numero do caractere 'a' (meu início) mais a chave inserida e tudo isso aplicado módulo 26. 
O módulo 26 é usado porque meu valor max é 26, e tudo que exceder o 26 deve reiniciar a contagem lá do meu primeiro valor.
6. retorno o valor encriptado para o main.py

- [X] Meu código de decriptar (decripta.py):
1. tem parâmetros de mensagem criptografada e chave que veem do código principal 'main.py'
2. listei o alfabeto em string (novamente porque este é outro código) para ser consultada a localização de cada letra necessária.
3. criei uma variável 'codigoDecriptado' para receber a mensagem original
4. Aqui eu apliquei a lógica de módulo (contudo não consigo fazer módulo de valores menores que 0, então fiz subtraindo os valores dos caracteres. Mas eu não subtraio realmente o valor, eu trabalho proporcionalmente inverso a encriptar: eu pego o valor da letra, somo 26 e diminuo o valor da chave para aplicar o módulo; desta forma ele faz a volta na string e daí sim eu consigo aplicar encontrar a letra original. Se eu diminuisse do valor da letra codificada literalmente, estouraria o range da minha string alfabeto.
5. retorno o valor decriptado para o main.py

- [X] Prints do teste de mesa:

![image](https://user-images.githubusercontent.com/56809101/197913979-adfc495e-710a-4a1c-8001-eac9ef038920.png)
![image](https://user-images.githubusercontent.com/56809101/197914119-b74c13cc-eeeb-41f6-a07b-43a0b80785e7.png)
![image](https://user-images.githubusercontent.com/56809101/197914167-7fc77590-0a41-49f3-acba-b3e1e6360315.png)
![image](https://user-images.githubusercontent.com/56809101/197914196-654facab-535e-42c5-8a9a-5c4f78714f06.png)
![image](https://user-images.githubusercontent.com/56809101/197914218-5f168666-02e8-4b00-8dfc-3cf36c237fab.png)
![image](https://user-images.githubusercontent.com/56809101/197914230-4f553234-9cf3-4977-9480-fe1ff504f23e.png)









