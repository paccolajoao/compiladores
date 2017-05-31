comentario_multiplas = False # Definida como global pois ela não pode ser resetada a cada linha
palavrasReservadas = [ "and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "func", "goto", "if", "in", "label", "mod", "not", "of", "or", "packed", "process", "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with", "integer", "real", "writeln", "readln", "char", "showmessage", "uses"]
simbolos_especiais = [ '+', '-', '*', '/', '=', ',', ';', ':', '<', '>', '(', ')', '{', '}', '.', '|',':=', '>=','<=', '<>', '!', '~', '<<', '>>', '+=', '-=', '*=', '/=']
token_especiais = [ "ADICAO", "SUBTRACAO", "MULTIPLICACAO", "DIVISAO", "IGUAL", "VIRGULA", "PONTO_VIRGULA", "DOIS_PONTOS", "MENOR", "MAIOR", "ABRE_PARENTESES", "FECHA_PARENTESES", "ABRE_CHAVES", "FECHA_CHAVES", "PONTO", "BARRA","DOIS_PONTOS_IGUAL", "MAIOR_IGUAL", "MENOR_IGUAL", "DIFERENTE", "NOT", "INVERTE_BIT", "DESLOCA_ESQUERDA", "DESLOCA_DIREITA","SOMA_ATRIBUI","SUBTRAI_ATRIBUI","MULTIPLICA_ATRIBUI", "DIVIDE_ATRIBUI"]


class analise_lexica():
    def analisador(self, text, line, vector_aux, line_aux):
        aux_string = ''
        dois_pontos_igual = False
        lendo_string = False
        comentario_linha = False
        numero_real = False;
        global comentario_multiplas # Definir pro Python que ele deve usar a variavel global

        for i in range(len(text)):
            # Verifica se é começo ou final de comentario de uma ou duas linhas
            if((text[i]=='{' or (text[i]=="(" and text[i+1]=='*')) and comentario_multiplas==False):
                comentario_multiplas = True

            elif((text[i]=='/' and text[i+1]=='/') and comentario_linha==False):
                comentario_linha = True


            if(comentario_linha==False and comentario_multiplas==False):
                # Verifica se está lendo string, e se estiver, adiciona a letra (incluindo espaço)
                if(lendo_string):
                    aux_string = aux_string + text[i];
                # Senão, vê se o text[i] não é espaço e se for, nem coloca
                elif(text[i] != ' '):
                    aux_string = aux_string + text[i];

                if(numero_real):
                    numero_real = False

                elif(dois_pontos_igual):
                    dois_pontos_igual = False
                    aux_string = ''

                # verifica se o igual está ligado a um ponto
                elif((i < (len(text) -1) and (text[i]+text[i+1]) in simbolos_especiais)):
                    dois_pontos_igual = True
                    aux_string = aux_string + text[i+1]
                    vector_aux.append(aux_string)
                    line_aux.append(line)

                # verifica se o número é float e precisa continuar a ler
                elif(aux_string.isdecimal() and text[i+1] == '.'):
                    #print(aux_string, '   ' , text[i+1] =='.')
                    numero_real = True;
                # verifica se o número é floa

                #compara para ver se é um limitador - pode ser melhorado!
                elif(aux_string in simbolos_especiais or text[i] in simbolos_especiais):
                    #pega o simbolo e coloca vazio no lugar, para não salvar o simbolo junto com a palavra
                    aux_string = aux_string.replace(text[i], '')
                    #verifica se aux_string é diferente de vazio, se for, coloca no vetor
                    if(aux_string != ''):
                        vector_aux.append(aux_string)
                        line_aux.append(line)
                    #coloca o simbolo no vetor
                    vector_aux.append(text[i])
                    line_aux.append(line)
                    #zera o aux_string, para pegar a proxima palavra
                    aux_string = ''

                # Se estiver lendo string e encontrar outro ', parar de ler string e adicionar cadeia na tabela
                elif(lendo_string == True and text[i]=='\''):
                    lendo_string = False
                    vector_aux.append(aux_string)
                    line_aux.append(line)
                    aux_string = ''

                # Se encontrar ' e nao estiver lendo string, começar a ler
                elif(text[i]=='\'' and lendo_string == False):
                    lendo_string = True

                #se for espaço (que é um limitador e não temos que guardar)
                elif (text[i] == ' ' and aux_string != '' and lendo_string == False):
                    vector_aux.append(aux_string)
                    line_aux.append(line)
                    aux_string = ''

            # Verifica se encontrou um fim de comentario
            if((text[i]=='}' or (text[i-1]=="*" and text[i]==')')) and comentario_multiplas==True):
                comentario_multiplas = False

        #se a linha estiver sozinha (não tendo nenhum limitador) salva a palavra
        if(aux_string != ''):
            vector_aux.append(aux_string)
            line_aux.append(line)
            aux_string = ''



    # define o vetor onde irá conter as palavras e simbolos reservados
    def tabela_tokens(self, vector_aux,lex_table,line_aux):
        index_aux = 1 # Variável para numeração de identificadores
        for i in range(len(vector_aux)):
            if((vector_aux[i][0] is "'")):
                lex_table.append('CADEIA DE CARACTERES')

            # Se a primeira letra for um numero, tem que ser um numero inteiro ou real
            elif(vector_aux[i][0].isdecimal() == True):
                # Passa pela palavra verificando se tem ponto ou letra
                ponto = False;
                erro = False;
                for char in vector_aux[i]:
                    if(char == "." and ponto == False):
                        ponto = True;
                    elif(char == "." and ponto == True):
                        erro = True;
                        # Erro de mais de um ponto no número, acusa erro
                    elif(char.isalpha() == True):
                        erro = True;

                if(erro == False):
                    if(ponto == True):
                        lex_table.append('NUMERO REAL')
                    else:
                        lex_table.append('NUMERO INTEIRO')
                else:
                    lex_table.append('NUMERO OU ID INVALIDO')

            # verifica se está em palavras reservadas e da um upper, que é a mesma coisa que pegar de outro vetor =D
            elif(vector_aux[i] in palavrasReservadas):
                lex_aux = palavrasReservadas.index(vector_aux[i])
                lex_table.append(palavrasReservadas[lex_aux].upper())

            # verifica se está em um simbolo especial e troca para a forma escrita
            elif(vector_aux[i] in simbolos_especiais):
                lex_aux = simbolos_especiais.index(vector_aux[i])
                lex_table.append(token_especiais[lex_aux])
            # verifica o resto que sobra, sem ser simbolo e palavra
            else:
                lex_table.append('Id')
                #lex_table.append('Id' + str(index_aux))
                index_aux += 1

        #printa quase em forma de tabela
        #for x in range(len(vector_aux)):
          #print ('Token: ', lex_table[x],'\nLexema: ', vector_aux[x],'\nLinha:', line_aux[x],'\n')
pass