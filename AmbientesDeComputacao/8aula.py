'''
Título: 8ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 08/04/2024

'''
aminoacidos = {
     "A":  ("Alanina", "Ala"),
     "C":  ("Cisteina", "Cys"),
     "D":  ("Aspartato", "Asp"),
     "E":  ("Glutamato", "Glu"),
     "F" : ("Fenilalanina", "Phe"),
     "G" : ("Glicina", "Gly"),
     "H" : ("Histidina", "His"),
     "I" : ("Ispleucina", "Ile"),
     "L" : ("Leucina", "Leu"),
     "K" : ("Lisina", "Lys"),
     "M" : ("Metionina", "Met"),
     "N" : ("Asparangina", "Asn"),
     "P" : ("Prolina", "Pro"),
     "Q" : ("Glutamina", "Gin"),
     "R" : ("Argenina", "Arg"),
     "S" : ("Serina", "Ser"),
     "T" : ("Treonina", "Thr"),
     "V" : ("Valina", "Val"),
     "W" : ("Triptofano", "Trp"),
     "Y" : ("Tirosina", "Tyr")
} 

print(aminoacidos)

for i in aminoacidos:
    #Aparece só o valor 
    print(aminoacidos[i])
    #aparece o valor e a chave 
    print(i, "=>", aminoacidos[i])
#Conseguir acessar dicionarios dentro dicionario
#print(aminoacido["A"]["ALA"])


#Conseguir chaves
for i in aminoacidos.keys():
    print(i)

for i in aminoacidos.values():
    print(i)

for chave, valor in aminoacidos.items():
     print(chave, "=>", valor)

#saber se uma chave exite
buscar = "D"
for i in aminoacidos:
    if i == buscar:
        print(f"Chave {buscar}") 


###ARQUIVOS
#Fechadno arquivos
#Arquivos armazeman permanemente resultados de um determinado  script 
#Analisar os dibersos formatos de arquivos oriundos dos programas de análise em bioinformática
#Leo um arquivo 
#open(nome, modo de abertura)  
#Modos de aberturas
#formato de leitura (r), escrita (w), adicionar infomrações (a), 
#codificação do arquivos, open(mone, modo, encoding = "UTF-8")
#Metodos para ler o arquivo
#Metodo read()
arquivo = open("/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/meu_arquivo.txt")
texto = arquivo.read()
print(texto)

#Metodo readline()
arquivo = open("/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/meu_arquivo.txt")

linha1 = arquivo.readline()
print(linha1)

linha2 = arquivo.readline()
print(linha2)

#Metodos readlines() vai jjogar numa lista
arquivo = open("/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/meu_arquivo.txt")

linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
    print(linhas )

#Para fechar um arquivo quando eu termino.
arquivo.close()

#Delimitando  o escopo com with
nome_arquivo  = "/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/meu_arquivo.txt" 

with open("/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/meu_arquivo.txt") as arquivo:

    linhas = arquivo.readlines()
    
    for  linha in linhas:
        linha = linha.strip()
        print(linha)

#criando variavel
home = "/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/"
nome_arquivo = home + "./meu_arquivo.txt"


#Testo que quero gravar
#w.write("Texto gravado")
#w.close()

##Proponha um algoritimo  para ler um arquivo fasta
arquivo = open(arquivo.fasta)

for linha in linhas:
    linha  = linha.split(">")
    print(linhas)