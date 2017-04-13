import re
text = compile(open('test.pas').read())
palavrasReservadas = [ "and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "func", "goto", "if", "in", "label", "mod", "not", "of", "or", "packed", "process", "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with", "integer", "real", "writeln", "readln", "char", "showmessage"]
simbolosespeciais = [ '+', '-', '*', '/', '=', ',', ';', ':', '<', '>', '(', ')', '{', '}', '.', '|' ]
token = [ "AND", "ARRAY", "BEGIN", "CASE", "CONST", "DIV", "DO", "DOWNTO", "ELSE", "END", "FILE", "FOR", "FUNC", "GOTO", "IF", "IN", "LABEL", "MOD", "NOT", "OF", "OR", "PACKED", "PROCESS", "PROGRAM", "RECORD", "REPEAT", "SET", "THEN", "TO", "TYPE", "UNTIL", "VAR", "WHILE", "IF", "INTEGER", "REAL", "WRITELN", "READLN", "CHAR", "SHOWMSG" ]
print(text.search('Oi'))
