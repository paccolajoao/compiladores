class analise_sintatica():
	
	def program(self, token, line_aux,k):
		if(token[k] == 'PROGRAM'):
			k = k+1
			if(token[k] == 'Id'):
				k = k+1
				if(token[k] == 'PONTO_VIRGULA'):
					k = k+1
				else:
					print('Erro sintático na linha: ',line_aux[k])
					return False
			else:
				print('Erro sintático na linha: ',line_aux[k])
				return False
		else:
			print('Erro sintático na linha: ',line_aux[k])
			return False

		return True

	def const(self,token,line_aux,k):
		if(token[k] == 'CADEIA DE CARACTERES'):
			k = k+1;
		elif(token[k] == 'ADICAO' or token[k] == 'SUBTRACAO'):
			k = k+1;
			if(token[k] == 'Id' or token[k] == 'NUMERO INTEIRO' or token[k] == 'NUMERO REAL'):
				k = k+1;
			else: 
				print('Erro sintático na linha: ',line_aux[k])
				return False
		else:
			print('Erro sintático na linha: ',line_aux[k])
			return False

	pass
	def analisador(self, token, line_aux):
		self.program(token,line_aux,0)