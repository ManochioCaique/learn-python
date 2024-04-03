'''
Título: 6ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 01/04/2024

'''
#String é tipo de dado que armazena coleções de caracteries 
#Concatenação de string 
v1 = "Olá"
v2 = "Mundo"
print(v1 + v2)
# Selecionar partes de um strin usar [0 : 1]

seq = "ATCTATGCATCGTACAGCTAGCTACGTAGCTCGT"
#Converter tudo minusculo
minusculo = seq.lower()
print(minusculo)

#Converter tudo maiusculo
maiusculo = seq.upper()
print(maiusculo)

#Removendo espaçõs  no começo e no fim da string e caracteries especiais
#\n \t \r
seq1 = "  ATCTATGCATCGTACAGCTAGCTACGTAGCTCGT   \n \t \r"
seq_filtrada = seq1.strip()
print(seq_filtrada)

#converter string em lista 
seq2 = "ATCTATGCATCGTACAGCTAGCTACGTAGCTCGT"
seq_lista = seq2.split("-")
print(seq_lista)
#buscas dentro de substring
seq3 = "ATCT ATGC ATCG TACA GCTA GCTA CGTA GCTCGT"
busca = seq3.find('TACA')
print(busca)
#Substituir um fragmento da minha string 
seq4 = "ATCT ATGC ATCG TACA GCTA GCTA CGTA GCTCGT"
new_string = seq4.replace('GCTCGT', 'PYTHON-RULES')
print(new_string)

#Contar quando vezes um caracteries aparece na sequencia
seq5 = "ATCT ATGC ATCG TACA GCTA GCTA CGTA GCTCGT"
quantas = seq5.count("A")
print(quantas)

#trabalhando com arquivos 
#CSV para Excel  
arquivo_csv = """ A, B, C, D 
1,2,3,4
5,6,7,8
9,10,11,12
"""
linhas = arquivo_csv.split("\n")

for linha in linhas:
    #trocar virgulas por tabulação
    celulas = linha.replace(",", "\t")
    print(celulas)
#Com isso possso jogar no excel porque separou como se fosse naquele jeito
    
#Para pegar do excel e jogar no python
arquivo_csv = """ A       B       C       D 
1       2       3       4
5       6       7       8
9       10      11      12
"""
linhas = arquivo_csv.split("\n")

for linha in linhas:
    #trocar tabulação por virgula
    celulas = linha.replace("/t", ",")
    print(celulas)

#Dada uma sequencia de DNA calcule o conteúdo GC

dna = "ATCTATGCATCGTACAGCTAGCTACGTAGCTCGT"

quantidade_c = dna.count("C")
quantidade_g = dna.count("G")
total_de_base = len(dna)
print(total_de_base)
soma = quantidade_c + quantidade_c

pro = (100 * soma)/total_de_base
print(pro)

#Escreva um programa para pegar as tres primeira e tres ultimas posições
inicial = dna[0:3]
print(inicial)

final = dna[-3:34]
print(final)

#Determine se um substring esta presente em uma string 
posicao = dna.find("CAG")
print(posicao)

#Kmer analise ou analise de janela deslisante

seq = "AAACGCAAA" 
n = len(seq)
k = 3
kmers = []

for i in range(0, n - k + 1):
    kmers = seq[i:i+k]
    print(" "*i+kmers)


#LISTA
#lista é sempre sequencial e numerica