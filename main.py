#/usr/bin/python3
#Luis Fernando Uzai
#Luis Felipe Bueno
#Joao Pedro Paccola
from lex import analise_lexica
from sintax import analise_sintatica
#abre o arquivo pascal
text = (open('test.pas').read())
text = text.lower()
vector_aux = []
lex_table = []
line_aux = []

#separa todas as linhas em um vetor
text_lines = text.splitlines()
text_letters = []
#separa todas as letras das linhas em um vetor
for z in text_lines:
    text_letters.append(list(z))

#analise lexica
lex = analise_lexica()
for i in range(len(text_letters)):
    pass
    lex.analisador(text_letters[i], i+1, vector_aux,line_aux)
lex.tabela_tokens(vector_aux,lex_table,line_aux)

sintax = analise_sintatica();

sintax.analisador(lex_table, line_aux)
