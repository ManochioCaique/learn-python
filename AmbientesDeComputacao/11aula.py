'''
Título: 11ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 22/04/2024

'''
#Expressões regulares. serve para buscas em textos. 
import re 
string = "O rato roeu a roupa do rei de Roma."
busca = re.findall("[rR][^ \.]*", string)
print(busca)


"""lookahead negativa é quando eu quero buscar valores que começam de uma maneira, mas não quero que inclui a parte padrão
Nesse exemplo ele vai pegar o que tiver na frente mas não inclui =OS

(?<=OS=)[A-z]+\s[a-z]+

Esse aqui ele pega o que esta antes do codigo

[A-z]+\s[a-z]+(?=\sGN=)
"""
#exemplo 
var = "> shudsfnjskdfnuhfbvçfva OS=Bacillus sub huachdjscsdanvkjds"
busca1 = re.findall("(?<=OS=)[A-z]+\s[a-z]+", var)
print(busca1)

#search 
#findall sempre busca todos os item e retorna tudo que é encontrado . 
#Não consigo printar, tenho que fazer um loop 
#re.sub(expressão relgular, caracter que quero substituir, string).

#Qual expressão regular pode ser usada para trocar as virgulas por tabulações
#COmo implementar em python???

with open("/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/arquivo.csv") as arquivo_gene:
    ler = arquivo_gene.read()
    result = re.sub(",", "\t", ler)
    print(result)
