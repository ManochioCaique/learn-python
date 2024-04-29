#dia 29 (acha) que vai ser online e vai ter um exercício de 5 pontos

#funções são blocos de códigos reutilizaveis que executam uma tarefa específica

#pra fazer uma função (ora ora) que tu quer usar ela varias vezes, pra não ficar copiando e colando varias vezes

#diferente de um método ( variavel.metodo() )

def nome_da_funcao(parametro1, parametro2, parametro3): #declaração da função
    #geralmente sempre se coloca esse comentário de 3 linhas em baixo da declaração da função
    ''' Ajuda da função: nome_da_funcao
    Objetivo: exemplo de função que recebe 3 valores, soma eles e retorna 1
    
    Entrada: recebe três parametros parametr1, parametro2 e parametro3
    Saida: string/int com dados processados

    Uso: nome_da_funcao(parametro1, parametro2, parametro3)
    '''
    saida = parametro1 + parametro2 + parametro3 #metodologia da função / procedimentos
    
    return saida #retorno de dados, é diferente de print

#os parametros declarados podem ser diferentes das variaveis, mas precisa ter o mesmo numero de parametros e variaveis
#a variavel que você declarar dentro da função só existe dentro da função
v1 = 1
v2 = 2
v3 = 3

resultado = nome_da_funcao(v1, v2, v3) #variavel pra receber o resultado, sem ela a função não devolve nada

print(resultado)





def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1) #você pode chamar a propria função dentro dela mesma (sim, confuso)
        '''
        ele deixa as contas em aberto

        n=5 
        5 * fatorial n-1, como não calculou o fatorial de n-1 (4) ele vai calcular esse fatorial
        n=4
        4 * fatorial de n-1, como não calculou o fatorial de n-1 (3) ele vai calcular esse fatorial
        n=3
        3 * fatorial de n-1, como não calculou o fatorial de n-1 (2) ele vai calcular esse fatorial
        n=2
        2 * fatorial de n-1, como não calculou o fatorial de n-1 (1) ele vai calcular esse fatorial
        n=1
        como 1 o if returna 1, então ele finalmente entrega um numero total pra ele fazer as contas
        e ele começa a calcular todas as multiplicações
        '''
    
n = 5

print(n, "! =", fatorial(n))







aa = {
    "ALA":"A",
    "ARG":"R",
    'ASN':"N",
    'ASP':"D",
    'CYS':"C",
    'GLN':"Q",
    'GLU':"E",
    'GLY':"G",
    'HIS':"H",
    'ILE':"I",
    'LEU':"L",
    'LYS':"K",
    'MET':"M",
    'PHE':"F",
    'PRO':"P",
    'SER':"S",
    'THR':"T",
    'TRP':"W",
    'TYR':"Y",
    'VAL':"V",
    }

def converter_3x1(a3):
    #recebe um codigo de 3 letras e devolve um codigo de 1 letra
    
    try: #tentar executar esse código
        a1 = aa[a3] #procura no dicionario as tres letras
    except: #caso de erro, vai executar esse código, geralmente é um código com 100% de funcionar, pra garantir que não vai dar um erro
        a1 = "X" #devolve X caso não ache as tres letras
    
    return a1

v1 = "AST"
print(converter_3x1(v1))

aa1 = {} #dicionario auxiliar
for chave in aa: #isso inverte o dicionario de aminoácidos, os valores viram chave e as chaves viram valores
    valor = aa[chave]
    aa1[valor] = chave

def converter_1x3(a1):
    #recebe 1 letra e devolve o código de 3 letras
    try:
        a3 = aa1[a1]
    except:
        a3 = "X"

    return a3

print(converter_1x3("A"))









#caso tenha uma quantidade aleatória de parametros, que você não sabe quantos são
def soma(*numeros): #coloca esse * no parametro pra receber multiplos parametros, a variavel vira uma lista
    soma = 0
    for i in numeros:
        soma += i

    return soma

total = soma(1, 2, 3, 4, 5)
print(total)

'''
Caso tu queira inserir multiplos dicionarios são 2 * invés de 1 só
def multi_valores(*args, **kwargs):
    print("Argumentos posicionais (*args): ")
    for arg in args:
        print(arg)

    print("\n Argumetnos de palavras-chave (**kwargs): ")
    for kwarg in kwargs:
        print(kwarg)
não consegui copiar o código inteiro, falta algo muito importante aqui pra usar isso
'''








#converte um arquivo CSV em uma lista
def le_csv(arquivo):
    import csv
    #ler arquivo csv
    #abre o arquivo CSV em modo de leitura
    meu_csv = []
    with open(arquivo, newline = '') as arquivo_csv:
        #cria um objeto leitos CSV e especifique o quotechar como aspas duplas
        leitos_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"') #separa os itens por virgula e aspas

        #ignorar o cabeçalho se necessario
        next(leitos_csv)

        #itere pelas linhas do arquivo CSV
        for linha in leitos_csv:
            meu_csv.append(linha)

        return meu_csv
    
dados = le_csv("arquivo.csv")
print(dados)

'''
você pode importar outros arquivos python que você criou como

import meu_arquivo as variavel

então quando tu usar essa variavel, ele vai executar a função desse arquivo
'''

import soma as sm

valor = sm.soma(1, 20)

print(valor)













