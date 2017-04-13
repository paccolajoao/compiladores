class analise():
    def analisador(self, text):
        aux_string = ""
        pass
        for i in text:
            aux_string = aux_string + i;
            if(i == ';'or i=='+'or i== '-' or i == '*' or i== '/'or i== '=' or i== ',' or i== ';' or i== ':' or i== '<' or i== '>' or i== '('or i==')'):
                # print(i)
                aux_string = aux_string.replace(i, '')
                print(aux_string)
                vector_aux.append(aux_string)
                vector_aux.append(i)
                aux_string = ''

            elif (i == ' '):
                vector_aux.append(aux_string)
                aux_string = ''

pass

text = (open('test.pas').read())

palavrasReservadas = [ "and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "func", "goto", "if", "in", "label", "mod", "not", "of", "or", "packed", "process", "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with", "integer", "real", "writeln", "readln", "char", "showmessage"]

simbolos_especiais = [ '+', '-', '*', '/', '=', ',', ';', ':', '<', '>', '(', ')', '{', '}', '.', '|']

token = [ "AND", "ARRAY", "BEGIN", "CASE", "CONST", "DIV", "DO", "DOWNTO", "ELSE", "END", "FILE", "FOR", "FUNC", "GOTO", "IF", "IN", "LABEL", "MOD", "NOT", "OF", "OR", "PACKED", "PROCESS", "PROGRAM", "RECORD", "REPEAT", "SET", "THEN", "TO", "TYPE", "UNTIL", "VAR", "WHILE", "IF", "INTEGER", "REAL", "WRITELN", "READLN", "CHAR", "SHOWMSG" ]

text_lines = text.splitlines()
text_letters = []
for z in text_lines:
    text_letters.append(list(z))

vector_aux = []
yo = analise()
for i in text_letters:
    pass
    yo.analisador(i)

print (vector_aux)
