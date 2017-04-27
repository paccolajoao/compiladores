#/usr/bin/python3
class analise():
    def analisador(self, text):
        aux_string = ''
        dois_pontos_igual = False
        lendo_string = False

        for i in range(len(text)):
            #print(i,'  ',text[i])
            # Verifica se está lendo string, e se estiver, adiciona a letra (incluindo espaço)
            if(lendo_string):
                aux_string = aux_string + text[i];
            # Senão, vê se o text[i] não é espaço e se for, nem coloca
            elif(text[i] != ' '):
                   aux_string = aux_string + text[i];

            if(dois_pontos_igual):
                dois_pontos_igual = False
                vector_aux.append(aux_string)
                aux_string = ''

            # verifica se o igual está ligado a um ponto
            elif(text[i] == ':' and text[i+1] == '='):
                dois_pontos_igual = True

            #compara para ver se é um limitador - pode ser melhorado!
            elif(aux_string in simbolos_especiais or text[i] in simbolos_especiais):
                #pega o simbolo e coloca vazio no lugar, para não salvar o simbolo junto com a palavra
                aux_string = aux_string.replace(text[i], '')
                #verifica se aux_string é diferente de vazio, se for, coloca no vetor
                if(aux_string != ''):
                    vector_aux.append(aux_string)
                #coloca o simbolo no vetor
                vector_aux.append(text[i])
                #zera o aux_string, para pegar a proxima palavra
                aux_string = ''
            
            # Se estiver lendo string e encontrar outro ', parar de ler string e adicionar cadeia na tabela
            elif(lendo_string == True and text[i]=='\''):
                lendo_string = False
                vector_aux.append(aux_string)
                aux_string = ''

            # Se encontrar ' e nao estiver lendo string, começar a ler
            elif(text[i]=='\'' and lendo_string == False):
                lendo_string = True

            #se for espaço (que é um limitador e não temos que guardar)
            elif (text[i] == ' ' and aux_string != '' and lendo_string == False):
                vector_aux.append(aux_string)
                aux_string = ''


        #se a linha estiver sozinha (não tendo nenhum limitador) salva a palavra
        if(aux_string != ''):
            vector_aux.append(aux_string)
            aux_string = ''



    # define o vetor onde irá conter as palavras e simbolos reservados
    def tabela_tokens(self, vector_aux):
        index_aux = 1
        for i in range(len(vector_aux)):

            # verifica se está em palavras reservadas e da um upper, que é a mesma coisa que pegar de outro vetor =D
            if(vector_aux[i] in palavrasReservadas):
                lex_aux = palavrasReservadas.index(vector_aux[i])
                lex_table.append(palavrasReservadas[lex_aux].upper())

            # verifica se está em um simbolo especial e troca para a forma escrita
            elif(vector_aux[i] in simbolos_especiais):
                lex_aux = simbolos_especiais.index(vector_aux[i])
                lex_table.append(token_especiais[lex_aux])

            # verifica o resto que sobra, sem ser simbolo e palavra
            else:
                lex_table.append('Id' + str(index_aux))
                index_aux += 1
        #printa quase em forma de tabela
        for x in range(len(vector_aux)):
          print (lex_table[x], vector_aux[x])

#abre o arquivo pascal
text = (open('test.pas').read())

palavrasReservadas = [ "and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "func", "goto", "if", "in", "label", "mod", "not", "of", "or", "packed", "process", "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with", "integer", "real", "writeln", "readln", "char", "showmessage", "uses"]

simbolos_especiais = [ '+', '-', '*', '/', '=', ',', ';', ':', '<', '>', '(', ')', '{', '}', '.', '|',':=']

token_especiais = [ "ADICAO", "SUBTRACAO", "MULTIPLICACAO", "DIVISAO", "IGUAL", "VIRGULA", "PONTO_VIRGULA", "DOIS_PONTOS", "MENOR", "MAIOR", "ABRE_PARENTESES", "FECHA_PARENTESES", "ABRE_CHAVES", "FECHA_CHAVES", "PONTO", "BARRA","DOIS_PONTOS_IGUAL"]

vector_aux = []
lex_table = []

#separa todas as linhas em um vetor
text_lines = text.splitlines()
text_letters = []
#separa todas as letras das linhas em um vetor
for z in text_lines:
    text_letters.append(list(z))

#analise lexica
lex = analise()
for i in text_letters:
    pass
    lex.analisador(i)

#printa o vetor com todas as palavras para separar
lex.tabela_tokens(vector_aux)
