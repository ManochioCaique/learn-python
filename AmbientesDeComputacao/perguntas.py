#PERGUNTAS E RESPOSTAS DA ATIVIDADE ONLINE DO DIA 29/04.AMBIETES DE COMPUTAÇÃO



"""Assinale o tipo da variável a seguir:
var1 = "1"
a.
string
"""

"""Qual a palavra-chave usada para declarar funções em Python?
c.
def
"""

"""Qual o método responsável por baixar um arquivo de estruturas de macromoléculas 
usando o PDB ID como argumento de entrada?
a.
retrieve_pdb_file()
"""
"""Quando analisamos uma sequência de DNA, precisamos considerar a região que será codificada. 
Em sequências de DNA, em especial, devemos considerar uma combinação de três nucleotídeos
 (pois sequências de códons são formadas por trincas de nucleotídeos). 
 Isso da margem a um conceito bastante utilizado em análises de sequência em bioinformática: 
janela deslizante. Para a sequência GAGTTTTATC, quantas k-mers de tamanho 3 podem ser obtidos?
d.
8
"""
seq = "GAGTTTTATC" 
n = len(seq)
k = 3
kmers = []

for i in range(0, n - k + 1):
    kmers = seq[i:i+k]
    print(" "*i+kmers)

"""Corresponde ao mais popular Bio* project da atualidade:

a.
Biopython
"""
"""Em Python, uma cláusula é uma parte de uma estrutura de controle de fluxo. 
Cláusulas são fundamentais em Python para controlar o fluxo de execução do código 
e lidar com diferentes situações. Indique qual das opções a seguir corresponde a uma 
estrutura de controle responsável por interromper a execução de um laço de repetição 
imediatamente e continuar a execução do código após o fim do bloco correspondente ao laço.
d.
break
"""

"""Observe o código a seguir:

 from Bio import SeqIO

O módulo SeqIO é responsável por fazer o carregamento 
de sequências no Biopython. Qual o método usado para abrir arquivos FASTA?

d.
parse
"""

"""Qual comando a seguir pode ser usado para declarar uma sequência no Biopython?
c.
s = Seq("ATCG")
"""

"""A sequência GAGTT, quando dividida em k-mers de tamanho k=3, produz 3 substrings:
 GAG, AGT e GTT. Qual é a fórmula para calcular o número total de subsequências geradas 
 por uma janela deslizante?
 
c.
total_subsequencias = (n - k + 1)
"""

"""Qual a função Python usada em um objeto de arquivo para ler o conteúdo de um arquivo já 
aberto e armazená-lo em uma única string?


b.
read()

"""

"""Em Biopython, podemos considerar leitura de sequências primárias como o equivalente a um primeiro passo. 
Qual o módulo deve ser carregado para lidar com sequências?

b.
from Bio.Seq import Seq
"""

"""O que a expressão regular [A-Z]+ retorna?
e.
Qualquer letra ou combinação de letras que apareçam pelo menos uma vez desde que estejam em maiúsculo"""


"""Observe o código a seguir:

from Bio.Seq import Seq
sequencia = Seq("AGTACACTGGT")
print(sequencia.xyz()) # ACCAGTGTACT

Dos nomes a seguir, qual substitui o trecho xyz para que a resposta apresentada 
seja identico ao comentário indicado?

b.
reverse_complement
"""
from Bio.Seq import Seq
sequencia = Seq("AGTACACTGGT")
print(sequencia.reverse_complement()) # ACCAGTGTACT

"""Como você criaria uma lista contendo os quadrados dos números 
de 0 a 9 usando list comprehension?
e.
[i**2 for i in range(10)]"""
lista_com_quadrados = []

for i in range(0,10):
    quadrado = i**2
    lista_com_quadrados.append(quadrado)
    print(i, quadrado)

quadrados = [i**2 for i in range(0,10)]
print(quadrados)


"""Antes de carregar um arquivo de estruturas de 
proteínas no Biopython, você deve declarar um objeto 
do tipo parser. Se estiver carregando um arquivo cif, 
você pode fazer isso usando o código:
from Bio.PDB import *
parser = MMCIFParser()
estrutura = [...]

Qual código a seguir, realiza o carregamento do 
arquivo 1BGA.cif presente no mesmo diretório do script?

b.
parser.get_structure("1BGA", "1BGA.cif")"""

"""Qual método é usado para verificar o tamanho de uma lista?

a.
len()
"""

"""Qual é a função do operador "%" em Python?
d.
Calcular o módulo de uma divisão."""

"""Assinale o tipo da variável a seguir:
var1 = 1,2"

d.
tuple"""

var1 = 1,2
print(type(var1))

"""O que é Biopython?
b.
É uma biblioteca ou uma coleção de ferramentas para facilitar o 
desenvolvimento de aplicações para a 
Bioinformática utilizando a linguagem de programação Python."""


"""Observe o código a seguir:

texto = "Strings são objetos que armazenam cadeias de caracteres"

Em seguida, indique a alternativa que expressa o que será impresso na tela para o comando:

print(texto[-10:])

d.
caracteres"""

"""Em Python, qual a estrutura 
condicional usada para executar um bloco caso uma condição for atendida?

c.
if"""


"""Qual a função do módulo SeqIO usada para gravar arquivos em formato FASTA?
c.
SeqIO.write
"""

texto = "Strings são objetos que armazenam cadeias de caracteres"
print(texto[-10:])


"""Qual a função do módulo SeqIO usada para gravar arquivos em formato FASTA?
c.
SeqIO.write"""


"""A função GC() retorna o conteúdo GC de uma sequência.
 Qual módulo do Biopython armazena esta função?
 e.
Bio.SeqUtils"""

"""Qual a função Python usada para imprimir valores na tela?
c.
print()"""

"""Em Python, qual o laço de repetição usado para executar um bloco enquanto uma condição for verdadeira?

a.
while"""

"""O que a expressão regular [^0-9] retorna?

d.
Qualquer valor não numérico"""


"""Observe o código a seguir:

lista = [1, 2, 3]
print(lista[2]) 
O que será impresso na tela?

a.
3"""

lista = [1, 2, 3]
print(lista[2])



"""Observe o código a seguir:

protein = translate("AUGGCCAUUCGCAAGGGUGCCCGAUAG")
print(protein)

Ao executar este código, você esperava que a sequência de proteína MAIRKGAR* 
fosse impressa na tela. Mas isso não acontece. Indique qual alternativa a 
seguir melhor explica o motivo disso não acontecer.
d.
O método translate deve ser aplicada a um objeto de sequência e não requer argumento de entrada."""

sa = Seq("AUGGCCAUUCGCAAGGGUGCCCGAUAG")
protein = sa.translate()
print(protein)

"""Dado um script Python, você deseja criar um dicionário para armazenar os códigos de uma letra de todos os 20 aminoácidos conhecidos. Como você adicionaria um novo item "Glicina" ao dicionário aminoacidos com a chave 'G'?

c.
aminoacidos['G'] = 'Glicina'

"""


"""Qual a saída do código abaixo:

DNA = 'TGATCGCCGA'
tamanho = float(len(DNA))
C = DNA.count('C')
G = DNA.count('G')
print(float((C+G)/tamanho)*100) # GC CONTENT

d.
60.0"""

DNA = 'TGATCGCCGA'
tamanho = float(len(DNA))
C = DNA.count('C')
G = DNA.count('G')
print(float((C+G)/tamanho)*100)

"""Observer o código a seguir:

1. valor_de_pi = 3.14
2. valor_de_pi = str(valor_de_pi)
3. print(valor_de_pi + valor_de_pi)

O que será impresso na tela?
e.
3.143.14
"""

valor_de_pi = 3.14
valor_de_pi = str(valor_de_pi)
print(valor_de_pi + valor_de_pi)


"""Observe o código a seguir:

a = "biscoito"
b = 2
soma = a+b

Ao executar este código, você obterá um erro. Qual tipo de erro?

c.
TypeError"""

"""Qual o método do Biopython pode ser usado para transcrever 
um objeto de sequência que armazena uma string de DNA em RNA?
a.
transcribe()"""

ata = Seq("ATCTGATGCTATTTTTTTTTT")

nova = ata.transcribe()
print(nova)

"""Qual o módulo do Biopython responsável pela 
manipulação de estrututas de proteínas?

c.
Bio.PDB
"""