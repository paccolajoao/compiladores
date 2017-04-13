
text = (open('test.pas').read())

palavrasReservadas = [ "and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "func", "goto", "if", "in", "label", "mod", "not", "of", "or", "packed", "process", "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with", "integer", "real", "writeln", "readln", "char", "showmessage"]

simbolos_especiais = [ '+', '-', '*', '/', '=', ',', ';', ':', '<', '>', '(', ')', '{', '}', '.', '|']

token = [ "AND", "ARRAY", "BEGIN", "CASE", "CONST", "DIV", "DO", "DOWNTO", "ELSE", "END", "FILE", "FOR", "FUNC", "GOTO", "IF", "IN", "LABEL", "MOD", "NOT", "OF", "OR", "PACKED", "PROCESS", "PROGRAM", "RECORD", "REPEAT", "SET", "THEN", "TO", "TYPE", "UNTIL", "VAR", "WHILE", "IF", "INTEGER", "REAL", "WRITELN", "READLN", "CHAR", "SHOWMSG" ]

text_letters = list(text);
aux_string = ""
simbolos_especiais_aux = ''
vector_aux = []

#print(simbolos_especiais_aux == '')

for j in simbolos_especiais:
	
	if(simbolos_especiais_aux == ''):
		simbolos_especiais_aux = '"' + simbolos_especiais_aux  + j + '"'
	
	else:
		simbolos_especiais_aux = simbolos_especiais_aux +   ' | ' + '"' + j + '"'

	#print(simbolos_especiais_aux)


for i in text_letters:
	aux_string = aux_string + i;
	
	if(i == (simbolos_especiais_aux)):
		print(i)

	elif i == ' ' | i == '\\n':
		vector_aux.append(aux_string)
		aux_string = ''
		print(vector_aux)

	else:
		print('Não achou')

