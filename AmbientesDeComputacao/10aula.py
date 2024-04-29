'''
Título: 10ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 17/04/2024

'''

"""Aula passada: programação procedural é um paradgma de programação lembrar que execução é linear (linha por linha)
as vezes vc vai precisar escrever partes repetidas usar modulização.

 FUNÇÕE

def nome( parametro):
    comandos 
"""

def soma (a, b):
    print(a + b)

soma(2, 2)

def soma1 (a, b):
    return a + b

somaa = soma1(2, 2)
print(f"A soma é {somaa}")

#para criar uma varial global :
#var = "adenina"

#global var 

#Retornar multiplos valores de uma vez. 

def soma_sub(a, b):
    return a + b, a - b

soma, subtracao  = soma_sub(1, 2)


#################################EXPRESSÕES REGULARES
#São  conhecidas rege RE ou ER são tecnicas para buscar padrões
#Modulo re 
#import re 

import re 
string = "O rato roeu a roupa do rei de Roma."

busca = re.findall("[rR][^\.]*", string)
print(busca)
#meta caracteries permitemque a construção de expressões regulares 
"""
.serve para buscar qualquer caracteres 
[] busca caracteres presentes na lista 
[^] busca caracteres não esteja na lista

ancoras 
^ busca no inicio de uma linha ou string 
$ busca no final de uma linha ou string 
quantificadores 
* buscar caracteres que aparecem varias veze ou nenhuma vezes 
? permite buscas que caracteries não aparece ou uma unica vez
+ aparece pelo menos uma vezes
{x , y}permite buscas por caracteres que aparecem várias vezes
outros 
| busca caracteries  a direita ou pelao caractere a esquerda
() permite a busca  por grupos de caracteres 
\ converter caracteres de metacaracteres em normal e vice e versa

"""
#como extrair os organismos desde arquivo fasta 
import re
var = "> shudsfnjskdfnuhfbvçfva OS=Bacillus sub huachdjscsdanvkjds"
busca = re.findall("OS=[a-zA-Z]* [a-z]*", var)
print(busca)
"""
re.search("expressão regular, texto que vou fazer a busca")
print(busca[0])

re.sub(espressão regular, substituição,  texto que quero fazer a busca)
"""

