'''
Título: 13ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 29/04/2024

'''
#Biopython biblioteca para trabalhar com dados genéticas 
#Vendo se biblioteca está instalada 
#caso não esteja usar !pip3 install biopython
#importando o biopython
import Bio

#Não é ideal importar todo o pacote, é melhor importar apenas as classes que vocÊ vai utilizar
from Bio.Seq import Seq
#O comando Seq cria um tipo especial de tipo sendo um asequência

seq1 = Seq("ATCGATGCTAGCTATACTGATCGATCGATCGATCAGCTAGCTAGCTAG")
print(type(seq1))

seq = "ATCGATGCTAGCTATACTGATCGATCGATCGATCAGCTAGCTAGCTAG"
print(type(seq))

#vendo tamanho
tamanho = len(seq1)
print(tamanho)

#conseguindo o reverso complementar da minha sequência
reverso_complementar = seq1.reverse_complement()
print(f"O reverso complementar é, {reverso_complementar}")

#Transcrever minha sequência
transcrever = seq1.transcribe()
print(f"A sequência transcrita é {transcrever}")

#Traduzir para ver se tem sequencia de aminoacido
traduzir = seq1.translate
print(f"A sequência da proteina é {traduzir}")

#Descobrindo posição de cada nucleotdeo
for i, n in enumerate(seq1):
    print(i,n)

#Procurando uma substring dentro da minha sequência
substring = seq1.count('ATCGATCGAT')
print(substring)

#reverter a string
print(seq1[::-1])

#Calcular o conteudo GC
from Bio.SeqUtils import GC 
print(GC(seq1))

#Converter objetos de sequência em strings
string = str(seq1)
print(type(string))

#Concatenar as duas sequências 
seq2 = Seq("AAATATATATATAGGCGCGAGAGATCGGAGATCG")
seqs = seq1 + seq2
print(seqs)
print(type(seqs))
print("\n\n\n\n\n\n")
#Trabalhando para importar arquivos 
#FASTA
#importando o SEIO
from Bio import SeqIO
#Salvando o caminho do arquivo nessa variável
seq_fasta = ("/home/caique/Documentos/Codigos/Python/learn-python/AmbientesDeComputacao/seq.fasta")
for i in SeqIO.parse(seq_fasta, "fasta"):
    print(i)

#IMprimindo apenas o ID
for i in SeqIO.parse(seq_fasta, "fasta"):
    print(i.id)

#Pegando id mais a seq
for i in SeqIO.parse(seq_fasta, "fasta"):
    print(i.id, ":", i.seq)


#Pegando id mais a descrição da sequencia 
for i in SeqIO.parse(seq_fasta, "fasta"):
    print(i.id, ":", i.description)

#Gravando informações importante em outro arquivo
#importando outro modulo pra fazer isso junto com SEQIO
from Bio.SeqRecord import SeqRecord
import re
gravar = []
for i in SeqIO.parse(seq_fasta, "fasta"):
    nome = i.id 
    descricao = i.description
    seq = i.seq
    #Coletando id do uniprot
    id_uniprot = re.findall("\|.*\|", descricao)
    id_uniprot = id_uniprot[0].replace("|", "")
    print(id_uniprot)
     #seqrecord 
    aux = SeqRecord(
        seq,
        id =  id_uniprot,
        description=''
    )
    gravar.append(aux)

print(gravar)
#Criando um novo arquivo fasta.
SeqIO.write(
    gravar,
    "seq2.fasta",
    "fasta"
)
print("\n\n\n\n\n\n")
print("\n\n\n\n\n\n")
#Traalhando com um arquivo PDB
from Bio.PDB import *
#pdb = PDBList()
#pdb.retrieve_pdb_file('4MDP')

parser = MMCIFParser()

estrutura = parser.get_structure('4mdp', '/home/caique/Documentos/Codigos/Python/learn-python/md/4mdp.cif')
print(estrutura)

# como vai ser analisado primeiro
#estrutura --> modelos --> cadeias --> residuoso --> átomos
#Para acessar o modelo
for modelo in estrutura:
    print(modelo)
    #para acessar as cadeia
    for cadeia in modelo:
        print(cadeia)
        #para acessar os residuos
        for residuo in cadeia:
            nome = residuo.get_resname()
            if nome != "HOH":
                print(nome, residuo.id[1])
            #para acessar os atomos           
            for atomo in residuo:
                print(atomo.coord)#coordenadas
                print(atomo.id)


#distancia euclidiana entre lys 475 e leu 468 - carbonos alfa
#[estrutura], [cadeia], [residuo], [atomo]
R1 = estrutura[0]['A'][475]['CA']   
R2 = estrutura[0]['A'][468]['CA']   
distancia = R1 - R2
print(distancia, "angstroms")